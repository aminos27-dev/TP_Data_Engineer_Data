import pandas as pd

URL = "https://raw.githubusercontent.com/kevinl75/tp-polytech-dataset/main/2025-09"

# Pour chaque fichier, on indique la colonne qui identifie une ligne
CLES = {
    "airports": "airport_id",
    "flights": "flight_id",
    "passengers_en": "passenger_id",
    "passengers_fr": "id_passager",
    "bookings": "booking_id",
}


def charger_jour(date):
    tableaux = {}
    for source in CLES:
        url_fichier = f"{URL}/{source}_{date}.csv"
        tableaux[source] = pd.read_csv(url_fichier, dtype="string")
    return tableaux


jour1 = charger_jour("2025-09-01")
jour2 = charger_jour("2025-09-02")

# Comparer chaque source entre le 1er et le 2 septembre
for source, cle in CLES.items():
    df1 = jour1[source]
    df2 = jour2[source]

    ids1 = set(df1[cle].dropna())
    ids2 = set(df2[cle].dropna())
    communs = sorted(ids1 & ids2)

    print(f"\n{source} (clé = {cle})")
    print("Lignes le 1er et le 2 =", len(df1), len(df2))
    print("Identifiants distincts le 1er et le 2 =", len(ids1), len(ids2))
    print("Identifiants communs =", len(communs))
    print("Présents seulement le 2 =", len(ids2 - ids1))
    print("Présents seulement le 1er =", len(ids1 - ids2))

    if communs:
        # Placer les mêmes identifiants dans le même ordre avant de comparer
        avant = df1.set_index(cle).loc[communs]
        apres = df2.set_index(cle).loc[communs]
        changements = avant.compare(apres)
        print("Identifiants dont les attributs ont changé =", len(changements))

# Comparer les sources de passagers EN et FR pour le 1er septembre
en = jour1["passengers_en"]
fr = jour1["passengers_fr"]

print("\nPassagers EN et FR du 1er septembre")
print("Colonnes EN =", en.columns.tolist())
print("Colonnes FR =", fr.columns.tolist())
print("Exemple de date de naissance EN =", en["birth_date"].iloc[0])
print("Exemple de date de naissance FR =", fr["date_naissance"].iloc[0])
print("Genres EN =", en["gender"].dropna().unique().tolist())
print("Genres FR =", fr["genre"].dropna().unique().tolist())

ids_en = set(en["passenger_id"].dropna())
ids_fr = set(fr["id_passager"].dropna())
print("Identifiants communs aux deux sources =", len(ids_en & ids_fr))

# Vérifier les dates de réservation contenues dans chaque fichier
print("\nDates de réservation")
print("Fichier du 1er =", jour1["bookings"]["booking_date"].unique().tolist())
print("Fichier du 2 =", jour2["bookings"]["booking_date"].unique().tolist())