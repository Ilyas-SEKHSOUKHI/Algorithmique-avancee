# Demander à l'utilisateur de saisir un mot
mot = input("Entrez un mot : ")

# Mettre le mot en minuscules pour éviter les différences entre majuscules/minuscules
mot = mot.lower()

# Inverser le mot à l'aide du slicing [::-1]
# Exemple : "ilyas" devient "sayli"
inverse = mot[::-1]

# Comparer le mot original et sa version inversée
# Si les deux sont identiques, alors c'est un palindrome
if mot == inverse:
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")
