from phonetics import soundex


def are_similar(text1:str, text2:str) -> bool:
    """Compare soundex coes of the two texts and returns True if they are similar.

    Args:
        text1 (str): Input text.
        text2 (str): Input text.

    Returns:
        bool: whether soundex codes are similar.
    """
    return soundex(text1) == soundex(text2)

def load_transliterated_names():
    # Pour l'instant je mets juste le résultat du LLM.
    return ['Avhusta', 'Husta', 'Avreliia', 'Aureliia', 'Aurika', 'Ahapia', 'Ahapia', 'Hafia', 'Hapka', 'Ahata', 'Agata', 'Ahlaia', 'Ahlaida', 'Ahnesa', 'Ahniia', 'Ahna', 'Ahrypyna', 'Horypyna', 'Hrunia', 'Adelaida', 'Adelina', 'Adelia', 'Adyla', 'Adel', 'Adriana', 'Andriana', 'Adrianna', 'Akylina', 'Kylina', 'Kulina', 'Yakylina', 'Alevtyna', 'Ala', 'Alia', 'Tina', 'Alina', 'Lina', 'Albertyna', 'Albertyna', 'Albyna', 'Alvyna', 'Anastasiia', 'Nastasiia', 'Nastia', 'Nasta', 'Nastka', 'Anatoliia', 'Anatolia', 'Anhelina', 'Anhela', 'Anhela', 'Anhela', 'Anhelika', 'Anhelika', 'Anhelina', 'Anna', 'Hanna', 'Annychka', 'Anka', 'Ania', 'Antonida', 'Antonida', 'Antonina', 'Tonia', 'Antonia', 'Anfisa', 'Anfysa', 'Arsena', 'Arseniia', 'Artemiziia', 'Artemisiia', 'Artemisa', 'Artemiza', 'Artemiia', 'Asklipiia', 'Asklepiia', 'Aurika', 'Aureliia', 'Avreliia', 'Afina', 'Atena', 'Afrodita', 'Afrodita', 'Bozhena', 'Bazhana', 'Beatrixa', 'Beata', 'Bohdana', 'Dana', 'Bohuslava', 'Slava', 'Boleslava', 'Boryslava', 'Bronislava', 'Valeriia', 'Lera', 'Lera', 'Lerunia', 'Lerusia', 'Lerusha', 'Lerochka', 'Varvara', 'Barbara', 'Vekla', 'Fekla', 'Teklia', 'Viktorina', 'Viktoriia', 'Vika', 'Vilena', 'Olena', 'Viola', 'Violanta', 'Violetta', 'Viola', 'Vita', 'Vitaliia', 'Vitalina', 'Vlada', 'Vladyslava', 'Slava', 'Volodymyra', 'Vseslava', 'Vyacheslava', 'Vyacheslava', 'Halyna', 'Halka', 'Halia', 'Hanna', 'Anna', 'Hafia', 'Ahapia', 'Helena', 'Helina', 'Hertruda', 'Herta', 'Gertruda', 'Hlafyra', 'Hlafyra', 'Hlafia', 'Fira', 'Hlykeriia', 'Lykeriia', 'Lykeria', 'Lukera', 'Horypyna', 'Ahrypyna', 'Agrypyna', 'Hustava', 'Husta', 'Gustava', 'Dana', 'Dania', 'Daniella', 'Daniella', 'Daryna', 'Odarina', 'Odarka', 'Darinia', 'Daria', 'Odarka', 'Daryna', 'Darka', 'Dariia', 'Daria', 'Dzvenyslava', 'Dzvinka', 'Zvenyslava', 'Diana', 'Dina', 'Domakha', 'Domna', 'Dorofeia', 'Doroteia', 'Dorofia', 'Evelina', 'Evelina', 'Edita', 'Edita', 'Elvyna', 'Albyna', 'Elvira', 'Emma', 'Emmanuila', 'Emmanuel', 'Emmanuela', 'Emiliia', 'Emilia', 'Esfir', 'Ester', 'Fira', 'Eva', 'Yevheniia', 'Yevhena', 'Yuhyna', 'Ivha', 'Yevdokiia', 'Dokiia', 'Yavdokha', 'Yevfrosyniia', 'Yefrosyniia', 'Frosyna', 'Frosia', 'Yelizaveta', 'Lizaveta', 'Lisaveta', 'Halishka', 'Halishka', 'Liza', 'Yepystymiia', 'Yepystyma', 'Pystyna', 'Zhadana', 'Zhdana', 'Zhanna', 'Ioanna', 'Ivanna', 'Ivanka', 'Zhozefina', 'Zhozefa', 'Zirka', 'Zira', 'Zoreslava', 'Zoryana', 'Zoria', 'Zoya', 'Oresta', 'Orina', 'Orisia', 'Orishka', 'Pavla', 'Pava', 'Pavlyna', 'Pavla', 'Pava', 'Pelagiia', 'Pelageia', 'Palahna', 'Palazha', 'Palazhka', 'Pazyna', 'Paraskeva', 'Paraskeviia', 'Paraskoviia', 'Paraska', 'Polina', 'Pavlyna', 'Apollinariia', 'Paulina', 'Priska', 'Yefrosyniia', 'Pulkheriia', 'Pulkhera', 'Radomyra', 'Radymyra', 'Raisa', 'Raia', 'Rakel', 'Rakhil', 'Rakhel', 'Roshel', 'Rebeka', 'Rebekka', 'Riia', 'Rianna', ' Rohvoloda', 'Rohneida', 'Rohniida', 'Roza', 'Ruzyna', 'Rozalia', 'Ruzalia', 'Roksana', 'Roksolana', 'Romana', 'Romanna', 'Romaniia', 'Rusudan', 'Rusudana', 'Rut', 'Ruf', 'Rufa', 'Rufyna', 'Rutyna', 'Rufyna', 'Rufima', 'Sara', 'Sarra', 'Svitlana', 'Lana', 'Svitozara', 'Sviatoiara', 'Sviatohora', 'Sviatoslava', 'Sekeleta', 'Sekeletyna', 'Simona', 'Simona', 'Solomiia', 'Salomeia', 'Sofiia', 'Zofiia', 'Sonia', 'Sofiia', 'Sofia', 'Stanislava', 'Stasia', 'Stania', 'Stella', 'Ela', 'Stefaniia', 'Stefanyda', 'Susanna', 'Susana', 'Sosanna', 'Zuzana', 'Suzanna', 'Sudyslava', 'Taisiia', 'Taisa', 'Tamara', 'Tamara', 'Teklia', 'Tekla', 'Fekla', 'Tereza', 'Tetiana', 'Tania', 'Tetiana', 'Tetiana', 'Tina', 'Troiana', 'Ustyna', 'Iustyna', 'Uliana', 'Uliana', 'Faina', 'Fevroniia', 'Fevrosiia', 'Khivria', 'Felitsiia', 'Feliksa', 'Fylitsata', 'Fylikitata', 'Fylitsitata', 'Feodora', 'Fedora', 'Todora', 'Feodosia', 'Fedosiia', 'Teodosiia', 'Fotyna', 'Fotiniia', 'Khotyna', 'Kharytyna', 'Kharytia', 'Kharyta', 'Khrysia', 'Khrysa', 'Khrystyna', 'Khrystia', 'Tsetsiia', 'Kekiliia', 'Tsvitana', 'Tsvetana', 'Iudita', 'Iudita', 'Iudif', 'Iudikhva', 'Iuzefa', 'Iuzefa', 'Iosyfa', 'Osyfa', 'Iuliia', 'Iulina', 'Iuliiana', 'Iuliianna', 'Iuliianiia', 'Iuniia', 'Iuna', 'Iustyna', 'Ustyna', 'Iukhymiia', 'Iukhymina', 'Iukhyma', 'Khymia', 'Iavdokha', 'Yevdokiia', 'Iana', 'Ivanna', 'Ianka', 'Ianina', 'Iaromyra', 'Iara']

def create_soundex_groups(names, surnames):
    soundex_groups={}
    for name,surname in zip(names,surnames):
        # print(name,surname)
        code = soundex(name) + soundex(surname)
        if code not in soundex_groups:
            soundex_groups[code] = [name+ " " + surname] # add name to the group
        else: soundex_groups[code].append(name + " " +  surname) #TODO put in dictionary name and surname

    return soundex_groups

def compute_nb_duplicated(soundex_groups):
    nb_duplicates=0
    for v in soundex_groups.values(): 
        nb = len(v)
        if nb>1: nb_duplicates+=nb
    return nb_duplicates

def graph_data_new(dataset, col_name="name", col_surname="surname"):
    """take the csv and output data for graph visualization"""

    names = dataset[col_name].to_list()
    surnames = dataset[col_surname].to_list()
    soundex_groups = create_soundex_groups(names, surnames)

    # Filter to only groups with potential duplicates
    duplicate_groups = {
        code: group for code, group in soundex_groups.items() 
        if len(group) > 1
    }

    # Recover data for HTML tootltip
    data_all_names = []
    id=1
    for p in dataset.iter_rows(named=True):
        data_all_names.append({
            'Original name': p["name"] + " " + p["surname"],
            'Transliterated name': p[col_name] + " " + p[col_surname],
            'expected': p["name_kmu"] + " " + p["surname_kmu"], #Official transliteration in the case of Ukrainian
            'soundex' : soundex(p[col_name]) + soundex(p[col_surname]), #soundex of transliterated name and surname.
            'id': id
        })
        id+=1

    result = {
        'duplicate_groups': duplicate_groups,
        'all_duplicates': data_all_names,
        'stats': {
            'total_records': len(dataset),
            'total_soundex_groups': len(soundex_groups),
            'duplicate_groups': len(duplicate_groups), #same as soundex groups. TODO : clean.
            'potential_duplicates': compute_nb_duplicated(soundex_groups)
        }
    }

    return result

# def create_soundex_groups_old(names):
#     soundex_groups={}
#     for name in names:
#         code = soundex(name) 
#         if code not in soundex_groups:
#             soundex_groups[code] = [name] # add name to the group
#         else: soundex_groups[code].append(name) #TODO put in dictionary name and surname

#     return soundex_groups

# def graph_data(transliterated_names):
#     """Take the result of soundex and put it in json for graph view

#     Args:
#         soundex_groups (_type_): _description_
#     """

#     soundex_groups = create_soundex_groups_old(transliterated_names)

#     # Filter to only groups with potential duplicates
#     duplicate_groups = {
#         code: group for code, group in soundex_groups.items() 
#         if len(group) > 1
#     }

#     # Prepare data for visualization
#     all_names = []
#     for group in duplicate_groups.values():
#         all_names.extend(group)

#     result = {
#         'duplicate_groups': duplicate_groups,
#         'all_duplicates': all_names,
#         'stats': {
#             'total_records': len(transliterated_names),
#             'total_soundex_groups': len(soundex_groups),
#             'duplicate_groups': len(duplicate_groups),
#             'potential_duplicates': len(all_names)
#         }
#     }

#     return result


if __name__ == "__main__":
    t_names = load_transliterated_names()  # à faire
    soundex_groups = create_soundex_groups(t_names)

    nb_duplicates=compute_nb_duplicated(soundex_groups)
    
    print("Before Levenshtein filtering:")
    print("=" * 60)
    print(f"Number of duplicates found = {nb_duplicates}")
    print(f"Percentage of duplicates found = {nb_duplicates/len(t_names)*100:.2f} %")


    
