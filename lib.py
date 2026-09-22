"""
But: Traiter une phrase pour determiner si la syntaxe est valide
Auteur: Nino BELAOUD, Nemo CHARPENTIER
Date: 22/09/2026
"""

# Constante des types de mots
ARTICLE = 0
ADJECTIF = 1
NOM_COMMUN = 2
VERBE = 3
NOM_PROPRE = 4
POINT = 5

# Table de transition
TRANSITIONS = [
    # art adj nom verbe npropre point
    [ 1, -1, -1, -1,  4, -1],  # 0
    [-1,  1,  2, -1, -1, -1],  # 1
    [-1,  2, -1,  3, -1, -1],  # 2
    [ 5, -1, -1, -1,  7,  9],  # 3
    [-1, -1, -1,  3, -1, -1],  # 4
    [-1,  5,  6, -1, -1, -1],  # 5
    [-1,  6, -1, -1, -1,  9],  # 6
    [-1, -1, -1, -1, -1,  9],  # 7
    [-1, -1, -1, -1, -1, -1],  # 8 pas utilisé, mais pour garder 9
    [-1, -1, -1, -1, -1, -1],  # 9 fin de phrase
    ]

# Dictionnaire pour l'analyse syntaxique
DICTIONNAIRE = {"le" : 0, "la" : 0, "chat" : 2, "souris" : 2, "martin" : 4,
"mange" : 3, "la" : 0, "petite" : 1, "joli" : 1, "grosse" : 1,
"bleu" : 1, "verte" : 1, "dort" : 3,"julie" : 4, "jean" : 4, "." : 5, "blanc": ADJECTIF}

# Liste des charactères ignorées du traitement
IGNORED = [
    ";",
    ":",
    ",",
]

"""
But: Extraire la listes des mots en minuscule en échappant les caractères spéciaux et sans les mots vides
Paramètres:
    - text (str) : texte duquel extraire les mots
Sorties: (list[str]) : liste des mots
"""
def extract_words(text: str):
    # =============================
    # Préparation du texte

    # Rajouter un espace avant un points
    text = text.replace(".", " .")

    # Echapper les caractères spéciaux
    for ignored in IGNORED:
        text = text.replace(ignored, " ")
    # =============================

    # Listes des mots
    words = []

    # Split le texte par ESPACE, sans les mots vides
    for word in text.split(" "):
        # Ignorer les vides
        if word == "":
            continue

        # Ajouter le mot en minuscule
        words.append(word.lower())

    return words

"""
But: Traiter une phrase pour savoir si elle est valide ou non
Paramètres:
    - text (str) : phrase à traiter
    - verbose (bool) : afficher les infos de débug
Sorties: (bool) : True si la phrase est valide, False sinon
"""
def process_text(text: str, verbose: bool):
    # Obtenir la liste de mots
    # Insérer un espace devant un point
    words = extract_words(text)

    # La position actuelle sur le graphe
    current_node = 0

    if verbose:
        print("-----------------------------------------")
        print(text)
        print(words)

    for word in words:
        if verbose:
            print("----------")
            print(f"Start : {current_node}")

        current_node = process_next_word(word, current_node, verbose)

        if verbose:
            print(f"Dest : {current_node}")

        # Fin de la phrase
        if current_node == 9:
            return True

        # Erreur
        if current_node == -1:
            return False

    return False

"""
But: Traiter le prochain mot pour savoir s'il est valide
Paramètres:
    - word (str) : mot à traiter
    - node (int) : noeud actuel
    - verbose (bool) : afficher les infos de débug
Sorties: (int) : noeud auquel mène le mot, -1 si le mot est invalide
"""
def process_next_word(word: str, node: int, verbose: bool):
    if verbose:
        print(f"  {word}")

    # Si le mot est inconnue alors INVALIDE
    if word not in DICTIONNAIRE:
        if verbose:
            print("  Unknown")

        return -1

    # Récupérer le type du mot
    word_type = DICTIONNAIRE[word]

    # Trouver la transition utilisé par le mot
    destination = find_destination(node, word_type)

    if verbose:
        print(f"  Type : {word_type}")

    # Si aucune transition trouvé alors INVALIDE
    if destination == None:
        return -1

    # Si une transition est trouvé alors on retourne sa destination
    return destination

"""
But: Trouver la destination depuis un noeud via un type
Paramètres:
    - node (int) : noeud actuel
    - type (int) : type utilisé pour la transition
Sortie: (int | None) : noeud de destination, None si aucune transition trouvée
"""
def find_destination(node: int, type: int):
    if node < 0 or node >= len(TRANSITIONS):
        return None

    if type < 0 or type >= len(TRANSITIONS):
        return None

    # Récupérer la destination
    destination = TRANSITIONS[node][type]

    return destination
