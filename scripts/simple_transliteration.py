#not sure we'll do this. Our problem is more dupicate matching. We can tackle the topic of transliteration but it's not as easy. 

# And since I already found 3 techniques for duplicate detection (levenshtein, Soundex, G2P models) then it's easier to be focused on that.

#Ok chef mais je vais le faire quand meme hihihi bc I can 
from transliterate import translit, get_available_language_codes
import cyrtranslit as ctlt 
import polars as p 

from names_translator import Transliterator

# loading csvs : 

UA_fem_name = p.read_csv("../create_dataset/ukr_female_names.csv")
UA_male_name = p.read_csv("../create_dataset/ukr_male_names.csv")
UA_surnames = p.read_csv("../create_dataset/ukr_surnames.csv")

#print(UA_surnames.head())

# Let's try both algorithms. 
# I want to take 10 lines from each dataset, transliterate each item
# store in dictionary and see wether some have 2 or more "items"

#using transliterate
dico = {}
print(get_available_language_codes())

df_translit = UA_fem_name.head(10)
for row in df_translit.iter_rows():
    for j in row :
        if j == None : 
            pass
        else : 
            t = translit(j,'uk', reversed = True)
            dico[t] = j 

print(dico)

# and now with cytranslit


dico_cy = {}
for row in df_translit.iter_rows():
    for j in row :
        if j == None : 
            pass
        else : 
            t = ctlt.to_latin(j, "ua")
            dico_cy[t] = j 

print(dico_cy)

# text = ["Дарія","Одарка","Дарина","Дарка","Дарья","Дар'я"]
# for k in text : 
#     print('Transliterate')
#     print(translit(k,'uk', reversed = True))
#     print('Cyrtransliterate')
#     print(ctlt.to_latin(k, "ua"))

#

tr = Transliterator()

text = ["Дарія","Одарка","Дарина","Дарка","Дарья","Дар'я"]
for k in text : 
    print('Ukrainians specific')
    print(tr.transliterate("",k,""))

# j'ai une erreur unicode ? je pense qu'il faut que je change qq chose mais idk how :) 
# run $env:PYTHONUTF8=1 from powershell

# can also try translit-ua package :)