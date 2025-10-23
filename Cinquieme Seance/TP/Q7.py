def fusionner_listes(L1, L2):
    resultat = []
    i = j = 0

    # Parcours des deux listes
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            resultat.append(L1[i])
            i += 1
        else:
            resultat.append(L2[j])
            j += 1

    # Ajouter les éléments restants
    while i < len(L1):
        resultat.append(L1[i])
        i += 1
    while j < len(L2):
        resultat.append(L2[j])
        j += 1

    return resultat
