import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

url = "https://uk.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%B8%D1%85_%D0%B6%D1%96%D0%BD%D0%BE%D1%87%D0%B8%D1%85_%D1%96%D0%BC%D0%B5%D0%BD"

# fix pour ne pas avoir le lien keblo !!
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "uk,en;q=0.9",
}

resp = requests.get(url, headers=headers)
resp.raise_for_status()

soup = BeautifulSoup(resp.text, "html.parser")

# Trouver tous les tableaux sur la page
tables = soup.find_all("table")

all_rows = []

for t in tables:
    # On lit le tableau avec pandas (c en ukrianien yupi)
    html_str = StringIO(str(t))
    try:
        df = pd.read_html(html_str, header=0)[0]
    except Exception:
        continue

    # Si les deux premières colonnes ressemblent à Ім'я / Варіанти (au cas ou)
    if df.columns.size >= 2 and "Ім" in str(df.columns[0]) and "Вар" in str(df.columns[1]):
        sub = df.iloc[:, :2].copy()
        sub.columns = ["Ім'я", "Варіанти"]
        all_rows.append(sub)

# Fusionner tous les tableaux détectés
if all_rows:
    result = pd.concat(all_rows, ignore_index=True)
else:
    result = pd.DataFrame(columns=["Ім'я", "Варіанти"])

# Nettoyage léger
result["Ім'я"] = result["Ім'я"].astype(str).str.strip()
result["Варіанти"] = result["Варіанти"].astype(str).str.strip()
result = result[result["Ім'я"] != ""]
result = result.drop_duplicates()

# Sauvegarde
result.to_csv("ukr_female_names.csv", index=False, encoding="utf-8-sig")

print(f"{len(result)} lignes extraites.")
print(result.head(10))

# Je vais refaire du cleaning dessus plus tard :) 

