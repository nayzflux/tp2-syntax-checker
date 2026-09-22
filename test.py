"""
But: Tester le programme
Auteur: Nino BELAOUD, Nemo CHARPENTIER
"""
import dictionary
import lib

# Dictionnaire utilisé pour le test
dictionnaire = dictionary.load_dictionary("data/dictionnaire1.csv")

# Afficher les messages de débug
verbose = True

# Process text
print("--------------------------------------")

print(" ")
print("process_text")
print(" ")

phrases_correctes = [
    "le joli chat mange.",
    "le ,joli chat ; dort.",
    "la grosse souris verte mange le joli petite chat blanc.",
    "la grosse souris verte mange jean.",
    "Jean dort.",
    "Jean mange Martin.",
    "Jean mange le chat.",
    "la verte souris grosse petit mange le bleu verte chat petite.",
]

phrases_incorrectes = [
    ".",
    "",
    "le joli chat mange",
    "le joli chat joue.",
]

for phrase in phrases_correctes:
    assert lib.process_text(phrase, dictionnaire, verbose), f"Devrait être correcte : {phrase}"

for phrase in phrases_incorrectes:
    assert not lib.process_text(phrase, dictionnaire, verbose), f"Devrait être incorrecte : {phrase}"

print("--------------------------------------")

print("Tous les tests sont passés.")
