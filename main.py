import polars as pl
from scripts import graph_data, export_for_visualization
from scripts import duplicates_levenshtein, create_list_fullnames

def main():
    print("Hello from reverse-engineering!")

    ## get database of names, surnames, and transliterations (csv format)

    #normalement ça vient de la DB mais trkl.

    UA_transliterated = pl.read_csv("data/UA_transliterated.csv", encoding="utf8")
    # transliterated_names_llm = ['Avhusta', 'Husta', 'Avreliia', 'Aureliia', 'Aurika', 'Ahapia', 'Ahapia', 'Hafia', 'Hapka', 'Ahata', 'Agata', 'Ahlaia', 'Ahlaida', 'Ahnesa', 'Ahniia', 'Ahna', 'Ahrypyna', 'Horypyna', 'Hrunia', 'Adelaida', 'Adelina', 'Adelia', 'Adyla', 'Adel', 'Adriana', 'Andriana', 'Adrianna', 'Akylina', 'Kylina', 'Kulina', 'Yakylina', 'Alevtyna', 'Ala', 'Alia', 'Tina', 'Alina', 'Lina', 'Albertyna', 'Albertyna', 'Albyna', 'Alvyna', 'Anastasiia', 'Nastasiia', 'Nastia', 'Nasta', 'Nastka', 'Anatoliia', 'Anatolia', 'Anhelina', 'Anhela', 'Anhela', 'Anhela', 'Anhelika', 'Anhelika', 'Anhelina', 'Anna', 'Hanna', 'Annychka', 'Anka', 'Ania', 'Antonida', 'Antonida', 'Antonina', 'Tonia', 'Antonia', 'Anfisa', 'Anfysa', 'Arsena', 'Arseniia', 'Artemiziia', 'Artemisiia', 'Artemisa', 'Artemiza', 'Artemiia', 'Asklipiia', 'Asklepiia', 'Aurika', 'Aureliia', 'Avreliia', 'Afina', 'Atena', 'Afrodita', 'Afrodita', 'Bozhena', 'Bazhana', 'Beatrixa', 'Beata', 'Bohdana', 'Dana', 'Bohuslava', 'Slava', 'Boleslava', 'Boryslava', 'Bronislava', 'Valeriia', 'Lera', 'Lera', 'Lerunia', 'Lerusia', 'Lerusha', 'Lerochka', 'Varvara', 'Barbara', 'Vekla', 'Fekla', 'Teklia', 'Viktorina', 'Viktoriia', 'Vika', 'Vilena', 'Olena', 'Viola', 'Violanta', 'Violetta', 'Viola', 'Vita', 'Vitaliia', 'Vitalina', 'Vlada', 'Vladyslava', 'Slava', 'Volodymyra', 'Vseslava', 'Vyacheslava', 'Vyacheslava', 'Halyna', 'Halka', 'Halia', 'Hanna', 'Anna', 'Hafia', 'Ahapia', 'Helena', 'Helina', 'Hertruda', 'Herta', 'Gertruda', 'Hlafyra', 'Hlafyra', 'Hlafia', 'Fira', 'Hlykeriia', 'Lykeriia', 'Lykeria', 'Lukera', 'Horypyna', 'Ahrypyna', 'Agrypyna', 'Hustava', 'Husta', 'Gustava', 'Dana', 'Dania', 'Daniella', 'Daniella', 'Daryna', 'Odarina', 'Odarka', 'Darinia', 'Daria', 'Odarka', 'Daryna', 'Darka', 'Dariia', 'Daria', 'Dzvenyslava', 'Dzvinka', 'Zvenyslava', 'Diana', 'Dina', 'Domakha', 'Domna', 'Dorofeia', 'Doroteia', 'Dorofia', 'Evelina', 'Evelina', 'Edita', 'Edita', 'Elvyna', 'Albyna', 'Elvira', 'Emma', 'Emmanuila', 'Emmanuel', 'Emmanuela', 'Emiliia', 'Emilia', 'Esfir', 'Ester', 'Fira', 'Eva', 'Yevheniia', 'Yevhena', 'Yuhyna', 'Ivha', 'Yevdokiia', 'Dokiia', 'Yavdokha', 'Yevfrosyniia', 'Yefrosyniia', 'Frosyna', 'Frosia', 'Yelizaveta', 'Lizaveta', 'Lisaveta', 'Halishka', 'Halishka', 'Liza', 'Yepystymiia', 'Yepystyma', 'Pystyna', 'Zhadana', 'Zhdana', 'Zhanna', 'Ioanna', 'Ivanna', 'Ivanka', 'Zhozefina', 'Zhozefa', 'Zirka', 'Zira', 'Zoreslava', 'Zoryana', 'Zoria', 'Zoya', 'Oresta', 'Orina', 'Orisia', 'Orishka', 'Pavla', 'Pava', 'Pavlyna', 'Pavla', 'Pava', 'Pelagiia', 'Pelageia', 'Palahna', 'Palazha', 'Palazhka', 'Pazyna', 'Paraskeva', 'Paraskeviia', 'Paraskoviia', 'Paraska', 'Polina', 'Pavlyna', 'Apollinariia', 'Paulina', 'Priska', 'Yefrosyniia', 'Pulkheriia', 'Pulkhera', 'Radomyra', 'Radymyra', 'Raisa', 'Raia', 'Rakel', 'Rakhil', 'Rakhel', 'Roshel', 'Rebeka', 'Rebekka', 'Riia', 'Rianna', ' Rohvoloda', 'Rohneida', 'Rohniida', 'Roza', 'Ruzyna', 'Rozalia', 'Ruzalia', 'Roksana', 'Roksolana', 'Romana', 'Romanna', 'Romaniia', 'Rusudan', 'Rusudana', 'Rut', 'Ruf', 'Rufa', 'Rufyna', 'Rutyna', 'Rufyna', 'Rufima', 'Sara', 'Sarra', 'Svitlana', 'Lana', 'Svitozara', 'Sviatoiara', 'Sviatohora', 'Sviatoslava', 'Sekeleta', 'Sekeletyna', 'Simona', 'Simona', 'Solomiia', 'Salomeia', 'Sofiia', 'Zofiia', 'Sonia', 'Sofiia', 'Sofia', 'Stanislava', 'Stasia', 'Stania', 'Stella', 'Ela', 'Stefaniia', 'Stefanyda', 'Susanna', 'Susana', 'Sosanna', 'Zuzana', 'Suzanna', 'Sudyslava', 'Taisiia', 'Taisa', 'Tamara', 'Tamara', 'Teklia', 'Tekla', 'Fekla', 'Tereza', 'Tetiana', 'Tania', 'Tetiana', 'Tetiana', 'Tina', 'Troiana', 'Ustyna', 'Iustyna', 'Uliana', 'Uliana', 'Faina', 'Fevroniia', 'Fevrosiia', 'Khivria', 'Felitsiia', 'Feliksa', 'Fylitsata', 'Fylikitata', 'Fylitsitata', 'Feodora', 'Fedora', 'Todora', 'Feodosia', 'Fedosiia', 'Teodosiia', 'Fotyna', 'Fotiniia', 'Khotyna', 'Kharytyna', 'Kharytia', 'Kharyta', 'Khrysia', 'Khrysa', 'Khrystyna', 'Khrystia', 'Tsetsiia', 'Kekiliia', 'Tsvitana', 'Tsvetana', 'Iudita', 'Iudita', 'Iudif', 'Iudikhva', 'Iuzefa', 'Iuzefa', 'Iosyfa', 'Osyfa', 'Iuliia', 'Iulina', 'Iuliiana', 'Iuliianna', 'Iuliianiia', 'Iuniia', 'Iuna', 'Iustyna', 'Ustyna', 'Iukhymiia', 'Iukhymina', 'Iukhyma', 'Khymia', 'Iavdokha', 'Yevdokiia', 'Iana', 'Ivanna', 'Ianka', 'Ianina', 'Iaromyra', 'Iara']

    ## Remove all ', " ", and č from all string columns
    for col in UA_transliterated.select(pl.col(pl.Utf8)).columns:
        UA_transliterated = UA_transliterated.with_columns(
            pl.col(col)
            .str.replace_all(r"[']", "")
            .str.replace_all(r"[č]", "ch")
            .str.replace_all(r"[š]","sh")
            .str.replace_all(r"[ĭ]","i")
            .str.replace_all(r"\s", "")
            .alias(col)
        )

    print(UA_transliterated)

    UA_transliterated.write_csv('data/UA_transliterated.csv')

    ## Compute soundex groups and json file

    # Ukrainian
    data_icu_UA = graph_data(UA_transliterated, col_name="name_icu", col_surname="surname_icu", output_file='json_viz/graph_data_icu_UA.json')
    data_llm_UA = graph_data(UA_transliterated, col_name="name_llm", col_surname="surname_llm", output_file='json_viz/graph_data_llm_UA.json')
    data_kmu_UA = graph_data(UA_transliterated, col_name="name_kmu", col_surname="surname_kmu", output_file='json_viz/graph_data_kmu_UA.json')



    ## compute statistics
    threshold=85 #levenshtein threshold

    n_names = data_icu_UA['stats']['total_records']
    n_groups = data_icu_UA['stats']['n_soundex_groups']
    n_soundex_merged = data_icu_UA['stats']['n_soundex_merges']

    list_soundex_merged = []
    for v in data_icu_UA["soundex_groups"].values():
        list_soundex_merged.extend(v)
    n_levenshtein_merged, list_levenshtein_merged = duplicates_levenshtein(create_list_fullnames(UA_transliterated,"name_icu","surname_icu"), threshold=threshold)
    print(f" is {n_levenshtein_merged} = 35 ?")
    print(list_levenshtein_merged)

    merged_soundex_levenshtein = list(set(list_soundex_merged) & set(list_levenshtein_merged))
    n_merged_soundex_levenshtein = len(merged_soundex_levenshtein)

    print("="*60)
    print(f"\nStats (method = ICU, language = Ukrainian):")
    print(f"  Number of names in dataset: {n_names}")
    print(f"  Number of clusters detected with Soundex: {n_groups}")
    print(f"  Duplicates detected with Soundex: {n_soundex_merged}")
    print(f"  Percentage of duplicates found with Soundex= {n_soundex_merged/n_names*100:.2f} %")
    print(f"  Percentage of duplicates found with Levenshtein (threshold={threshold}%)= {n_levenshtein_merged/n_names*100:.2f} %")
    print(f"  Percentage of duplicates found with both methods (threshold={threshold}%)= {n_merged_soundex_levenshtein/n_names*100:.2f} %")


    ###### stats llm

    n_names = data_llm_UA['stats']['total_records']
    n_groups = data_llm_UA['stats']['n_soundex_groups']
    n_soundex_merged = data_llm_UA['stats']['n_soundex_merges']

    list_soundex_merged = []
    for v in data_llm_UA["soundex_groups"].values():
        list_soundex_merged.extend(v)
    n_levenshtein_merged, list_levenshtein_merged = duplicates_levenshtein(create_list_fullnames(UA_transliterated,"name_llm","surname_llm"), threshold=threshold)

    merged_soundex_levenshtein = list(set(list_soundex_merged) & set(list_levenshtein_merged))
    n_merged_soundex_levenshtein = len(merged_soundex_levenshtein)

    print("="*60)
    print(f"\nStats (method = LLM, language = Ukrainian):")
    print(f"  Number of names in dataset: {n_names}")
    print(f"  Number of clusters detected with Soundex: {n_groups}")
    print(f"  Duplicates detected with Soundex: {n_soundex_merged}")
    print(f"  Percentage of duplicates found with Soundex= {n_soundex_merged/n_names*100:.2f} %")
    print(f"  Percentage of duplicates found with Levenshtein (threshold={threshold}%)= {n_levenshtein_merged/n_names*100:.2f} %")
    print(f"  Percentage of duplicates found with both methods (threshold={threshold}%)= {n_merged_soundex_levenshtein/n_names*100:.2f} %")


    ###### stats kmu

    n_names = data_kmu_UA['stats']['total_records']
    n_groups = data_kmu_UA['stats']['n_soundex_groups']
    n_soundex_merged = data_kmu_UA['stats']['n_soundex_merges']

    list_soundex_merged = []
    for v in data_kmu_UA["soundex_groups"].values():
        list_soundex_merged.extend(v)
    n_levenshtein_merged, list_levenshtein_merged = duplicates_levenshtein(create_list_fullnames(UA_transliterated,"name_kmu","surname_kmu"), threshold=threshold)

    merged_soundex_levenshtein = list(set(list_soundex_merged) & set(list_levenshtein_merged))
    n_merged_soundex_levenshtein = len(merged_soundex_levenshtein)

    print("="*60)
    print(f"\nStats (method = kmu, language = Ukrainian):")
    print(f"  Number of names in dataset: {n_names}")
    print(f"  Number of clusters detected with Soundex: {n_groups}")
    print(f"  Duplicates detected with Soundex: {n_soundex_merged}")
    print(f"  Percentage of duplicates found with Soundex= {n_soundex_merged/n_names*100:.2f} %")
    print(f"  Percentage of duplicates found with Levenshtein (threshold={threshold}%)= {n_levenshtein_merged/n_names*100:.2f} %")
    print(f"  Percentage of duplicates found with both methods (threshold={threshold}%)= {n_merged_soundex_levenshtein/n_names*100:.2f} %")


    

    ## Prepare data for graph visualization

    # viz_data = export_for_visualization(data, output_file='graph_data.json')
    # viz_data_icu_UA = export_for_visualization(data_icu_UA, output_file='json_viz/graph_data_icu_UA.json')
    # viz_data_llm_UA = export_for_visualization(data_llm_UA, output_file='json_viz/graph_data_llm_UA.json')
    # viz_data_llm_kmu = export_for_visualization(data_kmu_UA, output_file='json_viz/graph_data_kmu_UA.json')


    ## Visualize results with Levenshtein



if __name__ == "__main__":
    main()