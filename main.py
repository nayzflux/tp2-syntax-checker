from lib import process_text

"""
Programme principal
"""

# Recupere la phrase
phrase = input("Entrez une phrase : ")

# Analyse la phrase
valide = process_text(phrase, False)

# Affiche le resultat
if valide:
        print("Phrase correcte")
else:
        print("Phrase incorrecte")