#Afficher la fréquence de chaque lettre d’un mot.
# Demander à l'utilisateur d'entrer un mot
mot = input("Entrez un mot : ")

# Créer un dictionnaire pour stocker la fréquence des lettres
frequence = {}

# Parcourir chaque lettre du mot
for lettre in mot:
    # Convertir en minuscule pour ne pas différencier majuscule/minuscule
    lettre = lettre.lower()
    # Incrémenter le compteur
    if lettre in frequence:
        frequence[lettre] += 1
    else:
        frequence[lettre] = 1

# Afficher la fréquence de chaque lettre
for lettre, nb in frequence.items():
    print(f"Lettre '{lettre}' : {nb} fois")
