# from transliterate import translit, get_available_language_codes
# import cyrtranslit as ctlt 
import icu
import polars as pl 
import csv
# from names_translator import Transliterator

# Dataset structure : 
# language, name, surname

# Créer un dataset translitéré : langue, prénom, sa transliteration expected, sa (ses) transliteration(s) obetnue(s)

def build_ukrainian_dataset(dataset_name="test_dataset"):
    """build a dataset with :
    - language, 
    - name, surname, 
    - expected transliteration name, expected transliteration surname, 
    - obtained transliterations name and obtained transliterations surname (for different methods)
    This only creates the dataset for Ukrainian names. 
    We'll see if it will be extended to make it langauge agnostic (arabic?) 


    Args:
        dataset_name (str, optional): Name of the output dataset we want. Will be the name of the output CSV. Defaults to "test_dataset".

    Returns:
        polars dataframe: dataframe corresponding to the created csv dataset.
    """

    UA_fem_name = pl.read_csv("scripts/ukr_female_names.csv")
    # UA_male_name = p.read_csv("ukr_male_names.csv")
    UA_surnames = pl.read_csv("scripts/ukr_surnames.csv")

    # build the list of of lists of similar names:
    _, UA_fem_names_list  = build_list_of_lists(UA_fem_name)
    _, UA_surnames_list = build_list_of_lists(UA_surnames)


    # Initialize Transliterator(s)
    # Example with ICU
    tl_ukr = icu.Transliterator.createInstance('Any-Latin; Latin-ASCII') # ICU
    # from LLM_learned_transliteration import run_llm # LLM-based transliteration, still need to test.

    # Go through each list of lists and create name-surname pairs, and create the rows of the output dataset at the same time. 
    n = min(len(UA_fem_names_list), len(UA_surnames_list))

    with open(f"scripts/{dataset_name}.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["language","name","surname","expected_name_transliteration","expected_surname_transliteration","name_transliterations", "surname_transliterations", ]) #header

        for i in range(n):
            name, surname = UA_fem_names_list[i], UA_surnames_list[i]
            transliterated_name_icu, transliterated_surname_icu = tl_ukr.transliterate(name), tl_ukr.transliterate(surname) #instead of creating parallel list.
            # transliterated_name_llm, transliterated_surname_llm = run_llm(name, language="ukrainian", model="mistral-small3.2"), run_llm(surname, language="ukrainian", model="mistral-small3.2")
            
            # writer.writerow(["ukr",name,surname,"TBD","TBD",{"icu":transliterated_name_icu,"llm":transliterated_name_llm},{"icu":transliterated_surname_icu,"llm":transliterated_surname_llm}])
            writer.writerow(["UA",name,surname,"TBD","TBD",{"icu":transliterated_name_icu},{"icu":transliterated_surname_icu}])

    created_dataset = pl.read_csv(f"scripts/{dataset_name}.csv")

    return created_dataset

