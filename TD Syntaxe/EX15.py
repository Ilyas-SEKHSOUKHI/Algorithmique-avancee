#Trouver le mot le plus long dans une phrase donnée.
# Demander à l'utilisateur d'entrer un texte
texte = input("Entrez un texte : ")

# Diviser le texte en mots (séparés par des espaces)
mots = texte.split()

# Trouver le mot le plus long
plus_long = max(mots, key=len)

# Afficher le mot le plus long et sa longueur
print("Le mot le plus long est :", plus_long)
print("Sa longueur est :", len(plus_long))

