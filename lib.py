# Constante des types de mots
ARTICLE = 0
ADJECTIF = 1
NOM_COMMUN = 2
NOM_PROPRE = 4
VERBE = 3
POINT = 5

# Table de transition
NODES = [
    # Noeud 0
    [
        {
            "type": ARTICLE,
            "to": 1,
        },
        {
            "type": NOM_PROPRE,
            "to": 4,
        },
    ],

    # Noeud 1
    [
        {
            "type": ADJECTIF,
            "to": 1,
        },
        {
            "type": NOM_COMMUN,
            "to": 2,
        },
    ],

    # Noeud 2
    [
        {
            "type": ADJECTIF,
            "to": 2,
        },
        {
            "type": VERBE,
            "to": 3,
        },
    ],

    # Noeud 3
    [
        {
            "type": POINT,
            "to": 9,
        },
        {
            "type": ARTICLE,
            "to": 5,
        },
        {
            "type": NOM_PROPRE,
            "to": 7,
        },
    ],

    # Noeud 4
    [
        {
            "type": VERBE,
            "to": 3,
        },
    ],

    # Noeud 5
    [
        {
            "type": ADJECTIF,
            "to": 5,
        },
        {
            "type": POINT,
            "to": 6,
        },
    ],

    # Noeud 6
    [
        {
            "type": ADJECTIF,
            "to": 6,
        },
        {
            "type": POINT,
            "to": 9,
        },
    ],

    # Noeud 7
    [
        {
            "type": POINT,
            "to": 9,
        },
    ],

    # Noeud 8 : absent du graphe
    [],

    # Noeud 9 : état final
    [],
]

# Dictionnaire pour l'analyse syntaxique
DICTIONNAIRE = {"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5}

def process_text(text: str, verbose: bool):
    # Obtenir la liste de mots
    words = text.split(" ")

def process_next_word(text: str, node: int):
    type = DICTIONNAIRE[]
