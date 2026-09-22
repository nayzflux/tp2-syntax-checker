# Constante des types de mots
ARTICLE = 0
ADJECTIF = 1
NOM_COMMUN = 2
NOM_PROPRE = 4
VERBE = 3
POINT = 5

# Table de transition
transitions = [
    # art adj nom verbe npropre point
    [ 1, -1, -1, -1,  4, -1],  # 0  
    [-1,  1,  2, -1, -1, -1],  # 1 
    [-1,  2, -1,  3, -1, -1],  # 2 
    [ 5, -1, -1, -1,  7,  9],  # 3 
    [-1, -1, -1,  3, -1, -1],  # 4 
    [-1,  5,  6, -1, -1, -1],  # 5 
    [-1,  6, -1, -1, -1,  9],  # 6 
    [-1, -1, -1, -1, -1,  9],  # 7 
    [-1, -1, -1, -1, -1, -1],  # 8 inutilisé, gardé pour que la ligne 9 soit à l'indice 9
    [-1, -1, -1, -1, -1, -1],  # 9 fin de phrase
    ]

# Dictionnaire pour l'analyse syntaxique
DICTIONNAIRE = {"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

def process_text(text: str, verbose: bool):
    # Obtenir la liste de mots
    words = text.split(" ")

def process_next_word(text: str, node: int):
    type = DICTIONNAIRE[
