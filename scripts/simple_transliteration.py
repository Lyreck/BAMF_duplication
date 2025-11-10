#not sure we'll do this. Our problem is more dupicate matching. We can tackle the topic of transliteration but it's not as easy. 

# And since I already found 3 techniques for duplicate detection (levenshtein, Soundex, G2P models) then it's easier to be focused on that.

#Ok chef mais je vais le faire quand meme hihihi bc I can 

import transliterate as tlt
import cyrtranslit as ctlt 
import polars as p 

# loading csvs : 

UA_fem_name = p.read_csv("../create_dataset/ukr_female_names.csv")
UA_male_name = p.read_csv("../create_dataset/ukr_male_names.csv")
UA_surnames = p.read_csv("../create_dataset/ukr_surnames.csv")

print(UA_surnames.head())