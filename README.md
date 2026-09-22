# TP 2 : Analyseur de Syntaxe

## Auteurs

- Nemo CHARPENTIER
- Nino BELAOUD

## Présentation du projet

Ce projet consiste à réaliser en Python un analyseur syntaxique simple. Il détermine si une phrase respecte une grammaire volontairement limitée à l'aide d'un automate à états finis. Chaque mot est identifié grâce à un mini-dictionnaire (article, adjectif, nom, verbe ou nom propre), puis l'automate vérifie que leur enchaînement forme une phrase correcte et se termine par un point.

## Dictionnaire

Le programme utilise un dictionnaire pour associer chaque mot à son type grammatical.
Ce dictionnaire est chargé à partir d'un fichier CSV.

Deux dictionnaires sont fournis :

- [`dictionnaire.csv`](dictionnaire.csv) : dictionnaire minimal utilisé par défaut par le programme
- [`dictionnaire2.csv`](dictionnaire2.csv) : dictionnaire de 751 mots étendu depuis **Larousse**

```csv
mot,type
chat,2
mange,3
.,5
```

| Numéro | Type grammatical | Exemples |
|:---:|---|---|
| `0` | Article ou déterminant | `le`, `une`, `ces` |
| `1` | Adjectif | `joli`, `grande`, `bleu` |
| `2` | Nom commun | `chat`, `maison`, `livre` |
| `3` | Verbe conjugué | `mange`, `dort`, `regarde` |
| `4` | Nom propre | `jean`, `julie`, `paris` |
| `5` | Point final | `.` |

## Diagramme d'états et transition

![Graphe](Image/1screen.png)

Les états sont numéroté de **0 à 7** avec ***2 états spéciaux***

| Numéro | État |
|:----:|:---------:|
| -1 | Erreur |
| 9 | Correct |

### Table de transition

 Ce tableau donne le prochaine état selon l'état actuel et le type de mot

| État | 0 article | 1 adjectif | 2 nom | 3 verbe | 4 nom propre | 5 point |
|:----:|:---------:|:----------:|:-----:|:-------:|:------------:|:-------:|
| 0  | 1  | -1 | -1 | -1 | 4  | -1 |
| 1  | -1 | 1  | 2  | -1 | -1 | -1 |
| 2  | -1 | 2  | -1 | 3  | -1 | -1 |
| 3  | 5  | -1 | -1 | -1 | 7  | 9  |
| 4  | -1 | -1 | -1 | 3  | -1 | -1 |
| 5  | -1 | 5  | 6  | -1 | -1 | -1 |
| 6  | -1 | 6  | -1 | -1 | -1 | 9  |
| 7  | -1 | -1 | -1 | -1 | -1 | 9  |
| 8  | -1 | -1 | -1 | -1 | -1 | -1 |
| 9  | -1 | -1 | -1 | -1 | -1 | -1 |

```python
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
```

### Usage de l'IA

- Ecriture de la courte présentation du projet
- Génération de la matrice Python et du tableau Markdown depuis la table de transition
- Création d'un nouveau dictionnaire plus complet basé sur **Larousse**
