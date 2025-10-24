# Définir la phrase à analyser
phrase = "Ilyas SEKHSOUKHI"

# Définir les voyelles à rechercher
voyelles = "aeiou"  # on peut ajouter "y" si on veut le compter aussi

# Créer un dictionnaire qui associe chaque voyelle à son nombre d'occurrences
# - phrase.lower() met la phrase en minuscules (pour ignorer les majuscules)
# - phrase.lower().count(v) compte combien de fois la voyelle v apparaît
# - la boucle for v in voyelles parcourt chaque voyelle de la liste
counts = {v: phrase.lower().count(v) for v in voyelles}

# Calculer le total de voyelles trouvées
# counts.values() renvoie la liste des nombres d'occurrences
# sum() additionne tous ces nombres
total = sum(counts.values())

# Afficher le détail (nombre de chaque voyelle)
print("Détail :", counts)

# Afficher le total des voyelles
print("Total de voyelles (a,e,i,o,u) =", total)

