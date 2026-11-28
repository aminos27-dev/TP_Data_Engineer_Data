"""
À compléter : ingestion de l'entité `flights`, découpée en 3 fonctions bronze/silver/gold
(même structure que `ingest_airports.py`, à utiliser comme modèle).
"""
from datetime import date
from common import fetch_csv


def ingest_bronze(day: date = None, init: bool = False):
    # TODO : télécharger le snapshot flights du jour (ou de init/) vers bronze/.
    if init:
        fetch_csv("init", "flights.csv")
    else:
        assert day is not None
        nom_fichier = f"flights_{day.isoformat()}.csv"
        fetch_csv("2025-09", nom_fichier)


def create_silver_table(con):
    # TODO : créer silver_flights (colonnes du CSV source + is_active + deleted_date
    # + insert_timestamp/update_timestamp, cf. ingest_airports.py).
    raise NotImplementedError


def ingest_silver(day: date = None, init: bool = False):
    # TODO : chargement de la données dans silver_flights par flight_id 
    raise NotImplementedError


def ingest_gold():
    # TODO : reconstruire la/les table(s) de gold avec les données flights à partir de silver_flights
    raise NotImplementedError


def init():
    ingest_bronze(init=True)
    ingest_silver(init=True)
    ingest_gold()
    print("Vols (init) ingérés.")


if __name__ == "__main__":
    init()
