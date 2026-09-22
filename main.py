"""
But: Programme principal
Auteur: Nemo CHARPENTIER, Nino BELAOUD
"""

import dictionary
import lib

selection = input("Selectionnez un dictionnaire (1 ou 2 ou chemin) : ")

dictionnaire = ""

if selection == "1":
    dictionnaire = "data/dictionnaire1.csv"
elif selection == "2":
    dictionnaire = "data/dictionnaire2.csv"
else:
    dictionnaire = selection

dictionnaire = dictionary.load_dictionary(dictionnaire)

# Recupere la phrase
phrase = input("Entrez une phrase : ")

# Analyse la phrase
valide = lib.process_text(phrase, dictionnaire, False)

# Affiche le resultat
if valide:
    print("Phrase correcte")
else:
    print("Phrase incorrecte")
