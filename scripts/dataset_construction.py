# Surname source: https://www.kaggle.com/datasets/namecensus/name-census-top-100-surnames
# Name source: www.kaggle.com/datasets/namecensus/first-name-database

## Approche via API 

import polars as p
import kagglehub
from kagglehub import KaggleDatasetAdapter
import os

def load_kaggle_datasets():
    """ 
    Load name and surnames datasets from Kaggle with Kagglehub. Surname source: https://www.kaggle.com/datasets/namecensus/name-census-top-100-surnames. Name source: www.kaggle.com/datasets/namecensus/first-name-database.

    Parameters:

    Returns:
    Polars dataframe: Surnames in a polars dataframe
    Polars dataframe: Names in a polars dataframe
    """
    path_surnames = kagglehub.dataset_download("namecensus/name-census-top-100-surnames")
    path_names = kagglehub.dataset_download("namecensus/first-name-database")

    # Move files to clean location
    os.rename(path_surnames+"/surname-database.csv", "scripts/surname-database.csv")
    os.rename(path_names+"/first-name-database.csv", "scripts/first-name-database.csv")

    surnames= p.read_csv("scripts/surname-database.csv", separator=";")
    names = p.read_csv("scripts/first-name-database.csv", separator=";")

    return surnames, names

def clean_kaggle_datasets(surnames, names):
    """
    Remove unnecessary columns from the datasets surnames and names

    Parameters:
    surnames (polars dataframe): surnames in a polars dataframe
    names (polars dataframe): names in a polars dataframe

    Returns:
    Polars dataframe: cleaned surnames in a polars dataframe
    Polars dataframe: cleaned names in a polars dataframe
    """

    surnames = surnames.drop(["Country code", "Continent", "Official", "Country Rank"])
    names = names.drop(["Country code", "Continent", "Official", "Country Rank"])

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
    """build a dataset with language, name, surname, expected transliteration name, expected transliteration surname, obtained transliterations name and obtained transliterations surname.
    The last two columns are dicts since multiple methods can be used to transliterate, and it is more versatile to use dict than list.
    This only creates the dataset for Ukrainian names. We'll see if I extend the function to make it langauge agnostic, or if I just do multiple functions.


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
            writer.writerow(["ukr",name,surname,"TBD","TBD",{"icu":transliterated_name_icu},{"icu":transliterated_surname_icu}])

    created_dataset = pl.read_csv(f"scripts/{dataset_name}.csv")

    return created_dataset


def build_list_of_lists(df):
    """Transform a polars dataframe with names and given names of columns

    Args:
        df (polars dataframe): dataframe of origin, each line containing a name and its variants.

    Returns:
        list: list of lists. Each sub-list contains names (str) that are similar.
        list: list of all the names (str) in the dataframe.
    """

    l1= []
    l2 = []
    for row in df.rows(named=True):
        similar_names = []
        for key in df.columns:
            if row[key] not in ["", None]: #most of them are empty.
                similar_names.append(row[key])
                l2.append(row[key])

        l1.append(similar_names)
    
    return l1,l2



if __name__ == "__main__":
    
    # Kaggle
    # surnames, names = load_kaggle_datasets()
    # clean_kaggle_datasets(surnames, names)

    # Home-made name database
    df = build_ukrainian_dataset()

    print(df)
