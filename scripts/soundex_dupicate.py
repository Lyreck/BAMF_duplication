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


if __name__ == "__main__":
    t_names = load_transliterated_names()  # à faire
    soundex_dict={}
    unique_codes=[]
    for name in t_names:
        print(name)
        code = soundex(name)
        soundex_dict[f"{name}"] = soundex(name)
        if code not in unique_codes:
            unique_codes.append(code)
        
    print(f"Number of duplicate found = {len(t_names) - len(unique_codes)}")
    print(unique_codes)
    print(t_names)

    
