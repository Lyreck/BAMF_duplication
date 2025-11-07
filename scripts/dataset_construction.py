# Surname source: https://www.kaggle.com/datasets/namecensus/name-census-top-100-surnames
# Name source: www.kaggle.com/datasets/namecensus/first-name-database

## Approche via API 

import polars as p
import kagglehub
from kagglehub import KaggleDatasetAdapter

def load_datasets():
    """ 
    Load name and surnames datasets from Kaggle with Kagglehub. Surname source: https://www.kaggle.com/datasets/namecensus/name-census-top-100-surnames. Name source: www.kaggle.com/datasets/namecensus/first-name-database.

    Parameters:

    Returns:
    Polars dataframe: Surnames in a polars dataframe
    Polars dataframe: Names in a polars dataframe
    """
    path_surnames = kagglehub.dataset_download("namecensus/name-census-top-100-surnames")
    path_names = kagglehub.dataset_download("namecensus/first-name-database")

    surnames= p.read_csv(path_surnames+"/surname-database.csv", separator=";")
    names = p.read_csv(path_names+"/first-name-database.csv", separator=";")

    return surnames, names

def clean_datasets(surnames, names):
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



if __name__ == "__main__":
    surnames, names = load_datasets()
    clean_datasets(surnames, names)