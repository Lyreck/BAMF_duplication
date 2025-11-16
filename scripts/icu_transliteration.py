# Test transliteration with PyICU

# For compilers to find icu4c@77 you may need to set:
#  export LDFLAGS="-L/usr/local/opt/icu4c@77/lib"
#  export CPPFLAGS="-I/usr/local/opt/icu4c@77/include"

# For pkgconf to find icu4c@77 you may need to set:
#   export PKG_CONFIG_PATH="/usr/local/opt/icu4c@77/lib/pkgconfig"

# export CC="$(which gcc)" CXX="$(which g++)" (when installing ICU with homebrew)

# uv pip install --no-binary=:all: pyicu

# PyICU cheat sheet: https://gist.github.com/dpk/8325992

######################
# for translitua:
# Dictionary used (there are many): UkrainianKMU (National 2010, most recent one approved by The Cabinet)
# There are many language speicifc dictionaries as explained in Wikipédia: https://fr.wikipedia.org/wiki/Romanisation_de_l%27ukrainien
# But we prefer sticking to the official UA: https://czo.gov.ua/en/translit

import icu

def test_stackoverflow():
    tl = icu.Transliterator.createInstance('Any-Latin; Latin-ASCII')
    text = tl.transliterate('Ψάπφω')
    print(text) # 'Psappho'

def ukrainian_to_latin(text):
    """Transliteration of `text` from Ukrainian to Latin using PyICU (Python wrapper for ICU). An official transliteration can be obtained by looking at the Ukrainian government's
    website: https://czo.gov.ua/en/translit.

    Args:
        text (str): text to be transliterated, in ukrainian script.

    Returns:
        str: transliterated text in latin script.
    """
    # tl = icu.Transliterator.createInstance('Ukrainian-Latin; Latin-ASCII')
    tl = icu.Transliterator.createInstance('Cyrillic-Latin; Latin-ASCII')
    return tl.transliterate(text)

def arabic_to_latin(text):
    """Transliteration of `text` from Arabic to Latin using PyICU (Python wrapper for ICU). An official transliteration can be obtained by looking at the Ukrainian government's
    website: https://czo.gov.ua/en/translit.

    Args:
        text (str): text to be transliterated, in arabic script.

    Returns:
        str: transliterated text in latin script.
    """
    tl = icu.Transliterator.createInstance('Any-Latin; Latin-ASCII')
    return tl.transliterate(text)

if __name__ == "__main__":
    # Test code with a few ukrainian names.
    similar_names = ["Авраам","Авраамій","Аврамій", "Дарія","Одарка","Дарина","Дарка","Дарья","Дар'я"]
    for name in similar_names:
        latin_name = ukrainian_to_latin(name)
        print(f"{name} -> {latin_name}")

    # arabic_name = ["محمد"]
    # for name in arabic_name:
    #     latin_name = arabic_to_latin(name)
    #     print(f"{name} -> {latin_name}")