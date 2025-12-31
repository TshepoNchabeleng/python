import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    
    NP -> D N | N
    VP -> V | V NP
                              
    D -> "the" | "a" | "to" | "is"
    N -> "she" | "city" | "car" | "museum" | "zoo" | "home" | "taylor swift" | "music"
    V -> "saw" | "walked" | "listened" | "playing"

""")

parser = nltk.ChartParser(grammar)

sentence = input("Senetence: ").split()
try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
        tree.draw()
except ValueError:
    print("No parse tree possible.")