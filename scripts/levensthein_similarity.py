import Levenshtein
import polars as pl
# Code généré avec Le Chat.

def levenshtein_damerau_similarity(s1: str, s2: str) -> float:
    """
    Calcule le pourcentage de similarité entre deux chaînes
    en utilisant la distance de Levenshtein-Damerau,
    avec normalisation en minuscules (comme en JavaScript).
    """
    s1 = s1.lower()  # Normalisation en minuscules
    s2 = s2.lower()  # Normalisation en minuscules
    max_len = max(len(s1), len(s2))
    if max_len == 0:
        return 100.0
    distance = Levenshtein.distance(s1, s2)
    similarity = (1 - distance / max_len) * 100
    return round(similarity, 2)



def duplicates_levenshtein(strings: list[str], threshold: float = 80.0) -> int:
    """
    Calcule le nombre de nœuds uniques qui ont au moins une similarité
    supérieure ou égale au seuil avec une autre chaîne de la liste.

    Args:
        strings: Liste de chaînes de caractères.
        threshold: Seuil de similarité (en %).

    Returns:
        int: Nombre de nœuds uniques "liés" selon le seuil.
    """
    n = len(strings)
    unique_nodes_above_threshold = set()

    for i in range(n):
        for j in range(i + 1, n):
            sim = levenshtein_damerau_similarity(strings[i], strings[j])
            if (strings[i] in ["Artemisa Skrinnincenko", "Artemiza Skrinnicenko"]) and (strings[j] in ["Artemisa Skrinnincenko", "Artemiza Skrinnicenko"]):
                print(sim)
            if sim >= threshold:
                unique_nodes_above_threshold.add(i)
                unique_nodes_above_threshold.add(j)

    unique_nodes_above_threshold_list = [strings[i] for i in unique_nodes_above_threshold]
    return len(unique_nodes_above_threshold), unique_nodes_above_threshold_list


def create_list_fullnames(df: pl.DataFrame, col_name, col_surname):
    return df.with_columns(
                pl.concat_str([col_name, col_surname], separator=" ")
                .alias("fullname")
                )["fullname"].to_list()

if __name__ == "__main__":
    # Exemple d'utilisation
    s1 = "kitten"
    s2 = "sitting"
    similarity = levenshtein_damerau_similarity(s1, s2)
    print(f"Similarité : {similarity}%")

    # Similarity threshold test
    strings = ["kitten", "sitting", "kittens", "saturday", "sunday"]
    threshold = 70.0
    count = duplicates_levenshtein(strings, threshold)

    print(f"Nombre de nœuds uniques liés (seuil >= {threshold}%) : {count}")


    # Test avec les chaînes problématiques
    s1 = "Gafia Romanij"
    s2 = "Agafia Romaniv"
    similarity = levenshtein_damerau_similarity(s1, s2)
    print(f"Similarité : {similarity}%")