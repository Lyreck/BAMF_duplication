# Surname source: https://www.kaggle.com/datasets/namecensus/name-census-top-100-surnames
# Name source: www.kaggle.com/datasets/namecensus/first-name-database

## Approche via API 

import polars as p
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Download latest version
path_surnames = kagglehub.dataset_download("namecensus/name-census-top-100-surnames")
path_names = kagglehub.dataset_download("namecensus/first-name-database")

surnames= p.read_csv(path_surnames+"/surname-database.csv", separator=";")
surnames = surnames.drop(["Name ASCII", "Country code", "Continent", "Official", "Country Rank"])

names = p.read_csv(path_names+"/first-name-database.csv", separator=";")
names = names.drop(["Name ASCII", "Country code", "Continent", "Official", "Country Rank"])


print(names)


