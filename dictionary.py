"""
But: Importer un dictionnaire à partir d'un fichier CSV.
Auteur: Nino BELAOUD
Date: 22/09/2026
"""

import pandas as pd

"""
But: Charger un dictionnaire à partir d'un fichier CSV.
Entrée:
    - file_path (str) : Chemin vers le fichier CSV.
Sortie: Dictionnaire chargé à partir du fichier CSV.
"""
def load_dictionary(file_path: str):
    df = pd.read_csv(file_path)

    dictionary = {}

    for _, row in df.iterrows():
        mot = row["mot"]
        type_mot = row["type"]

        dictionary[mot] = type_mot

    return dictionary
