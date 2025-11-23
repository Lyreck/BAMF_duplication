from names_translator import Transliterator
import cyrtranslit as ctlt 
from translitua import translit, UkrainianKMU, UkrainianGerman, UkrainianBritish
from translit_llm import run_llm
# import icu
import polars as pl 
# Dataset structure : 
# language, name, surname

# Créer un dataset translitéré : langue, prénom, sa transliteration expected, 

#donc pour chaque type de traliteration, on va translit et garder la colonne

def cytranslit_fn(x: str) -> str:
    if x is None:
        return None
    return ctlt.to_latin(x, "ua")

def kmu_fn(x: str) -> str:
    if x is None:
        return None
    return translit(x, UkrainianKMU)

def german_fn(x: str) -> str:
    if x is None:
        return None
    return translit(x, UkrainianGerman)

def british_fn(x: str) -> str:
    if x is None:
        return None
    return translit(x, UkrainianBritish)

def icu_fn(x:str) -> str:
    tl = icu.Transliterator.createInstance('Any-Latin; Latin-ASCII')
    return tl.transliterate(x)

def llm_fn(x:str) -> str:
    return run_llm(x, "ukrainian", "mistral-small3.2")



def add_transliterations(df: pl.DataFrame, name_col="name", surn_col="surname"):
    return df.with_columns([
        pl.col(name_col).map_elements(cytranslit_fn).alias(f"{name_col}_cy"),
        pl.col(surn_col).map_elements(cytranslit_fn).alias(f"{surn_col}_cy"),

        pl.col(name_col).map_elements(kmu_fn).alias(f"{name_col}_kmu"),
        pl.col(surn_col).map_elements(kmu_fn).alias(f"{surn_col}_kmu"),

        pl.col(name_col).map_elements(german_fn).alias(f"{name_col}_de"),
        pl.col(surn_col).map_elements(german_fn).alias(f"{surn_col}_de"),

        pl.col(name_col).map_elements(british_fn).alias(f"{name_col}_br"),
        pl.col(surn_col).map_elements(british_fn).alias(f"{surn_col}_br"),

        pl.col(name_col).map_elements(llm_fn).alias(f"{name_col}_llm"),
        pl.col(surn_col).map_elements(llm_fn).alias(f"{surn_col}_llm"),
    ])

def add_transliterations_icu(df: pl.DataFrame, name_col="name", surn_col="surname"): #separate function bcz icu not on same computer
    
    return df.with_columns([
        pl.col(name_col).map_elements(icu_fn).alias(f"{name_col}_icu"),
        pl.col(surn_col).map_elements(icu_fn).alias(f"{surn_col}_icu")
    ])

if __name__ == "__main__":

    df = pl.read_csv("create_dataset/UA_paired.csv", encoding="utf8")

    df_out = add_transliterations(df)
    # df_out = add_transliterations_icu(df) #for machine with icu installed
    df_out.write_csv('UA_transliterated.csv')

    print(df_out)