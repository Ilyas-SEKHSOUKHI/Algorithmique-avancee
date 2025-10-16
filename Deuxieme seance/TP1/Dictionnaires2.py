# Données de base
notes = {"Ali": 12, "Sara": 15, "Lina": 9}

# Créer le dictionnaire "resultats"
resultats = {}
for key in notes:
    if notes[key] >= 10:
        resultats[key] = "Admis"
    else:
        resultats[key] = "Non admis"

print("Résultats :", resultats)

# Construire le dictionnaire inverse
inverse = {}
for etudiant, mention in resultats.items():
    if mention in inverse:
        inverse[mention].append(etudiant)
    else:
        inverse[mention] = [etudiant]

print("Inverse :", inverse)
