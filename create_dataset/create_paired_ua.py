# from transliterate import translit, get_available_language_codes
import icu
from collections import defaultdict
import random
import polars as pl 

from names_translator import Transliterator
import cyrtranslit as ctlt 
from translitua import translit, UkrainianKMU, UkrainianGerman, UkrainianBritish, RussianGOST2006


# ----------------------------------------------
# GROUP ROWS BY NUMBER OF VARIANTS
# ----------------------------------------------

def group_by_length(df: pl.DataFrame) -> dict[int, list[str]]:
    """
    Groups each row (canonical name + variants) by the number of
    non-empty entries in the row.
    
    Returns:
        dict { count: [ [name, variant1, variant2, ...], ... ] }
    """

    groups = defaultdict(list)

    for row in df.iter_rows():
        variants = [x for x in row if isinstance(x, str) and x.strip() != ""]
        if not variants:
            continue

        count = len(variants)
        groups[count].append(variants)

    return groups


# ----------------------------------------------
# BUILD PAIRED NAME / SURNAME VARIANT LISTS
# ----------------------------------------------

def build_name_pairs_from_groups(names_by_count: dict[int, list[list[str]]],
                                 surnames_by_count: dict[int, list[list[str]]]) -> list[dict]:
    """
    Creates pairs matching name rows with surname rows by variant count.
    If counts don't match, borrows from smaller groups.
    """

    pairs = []

    for s_count in sorted(surnames_by_count.keys(), reverse=True):
        surn_rows = surnames_by_count[s_count]

        for surn in surn_rows:

            if s_count in names_by_count and names_by_count[s_count]:
                name = names_by_count[s_count].pop(0)

            else:
                available_groups = [c for c in names_by_count if names_by_count[c]]
                if not available_groups:
                    raise ValueError("Ran out of names to match!")

                chosen = random.choice(available_groups)
                name = names_by_count[chosen].pop(0)

            pairs.append({
                "name_variants": name,
                "surname_variants": surn,
            })

    return pairs


# ----------------------------------------------
# SPLIT SURNAMES INTO FEMALE/MALE TARGET RATIOS
# ----------------------------------------------

def build_gender_balanced_pairs(female_names_by_count,
                                male_names_by_count,
                                surnames_by_count,
                                female_ratio=0.70):

    all_surname_rows = sum(len(v) for v in surnames_by_count.values())
    female_target = int(all_surname_rows * female_ratio)
    male_target   = all_surname_rows - female_target

    female_surns = {}
    male_surns = {}

    remaining_f = female_target

    for count in sorted(surnames_by_count.keys(), reverse=True):
        group = surnames_by_count[count]

        if remaining_f > 0:
            take_f = min(len(group), remaining_f)
            female_surns[count] = group[:take_f]
            remaining_f -= take_f
        else:
            female_surns[count] = []

        leftover = group[len(female_surns[count]):]
        male_surns[count] = leftover

    # Build separately
    female_pairs = build_name_pairs_from_groups(
        names_by_count={k: v.copy() for k, v in female_names_by_count.items()},
        surnames_by_count=female_surns
    )
    for p in female_pairs:
        p["gender"] = "female"

    male_pairs = build_name_pairs_from_groups(
        names_by_count={k: v.copy() for k, v in male_names_by_count.items()},
        surnames_by_count=male_surns
    )
    for p in male_pairs:
        p["gender"] = "male"

    all_pairs = female_pairs + male_pairs
    random.shuffle(all_pairs)

    return all_pairs


# ----------------------------------------------
# NEW: TIDY LONG OUTPUT  →  1 ROW PER VARIANT
# ----------------------------------------------

def pairs_to_long_df(pairs: list[dict], language: str = "uk") -> pl.DataFrame:
    """
    Converts pairs into a long Polars dataframe:
    one row per variant: gender, language, name, surname.
    """

    rows = []

    for p in pairs:
        gender = p["gender"]
        name_vars = p["name_variants"]
        surn_vars = p["surname_variants"]

        # zip ensures: variant1→variant1, variant2→variant2, etc.
        for nv, sv in zip(name_vars, surn_vars):
            rows.append({
                "gender": gender,
                "language": language,
                "name": nv,
                "surname": sv,
            })

    return pl.DataFrame(rows)

if __name__ == "__main__":

    # Load CSVs
    df_f = pl.read_csv('create_dataset/ukr_female_names.csv')
    df_m = pl.read_csv('create_dataset/ukr_male_names.csv')
    df_s = pl.read_csv('create_dataset/ukr_surnames.csv')

    # Group by variant length
    female_by = group_by_length(df_f)
    male_by   = group_by_length(df_m)
    surn_by   = group_by_length(df_s)

    # Build gender-balanced pairs
    pairs = build_gender_balanced_pairs(
        female_by,
        male_by,
        surn_by,
        female_ratio=0.70
    )

    # Convert to tidy long DF
    final_df = pairs_to_long_df(pairs, language="uk")
    final_df.write_csv("UA_paired.csv")

    print(final_df)