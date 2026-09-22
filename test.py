import lib

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
    "le joli chat joue",
    "le joli chat joue."
]

for phrase in phrases_correctes:
    print(phrase, lib.process_text(phrase, True) == True)

for phrase in phrases_incorrectes:
    print(phrase, lib.process_text(phrase, True) == False)
