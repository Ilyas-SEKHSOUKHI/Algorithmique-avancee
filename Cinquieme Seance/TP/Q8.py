def recherche_lineaire(tab, x):
    """
    Fonction qui retourne l'indice de la première occurrence de x dans le tableau tab,
    ou -1 si x n'est pas présent dans le tableau.
    
    Args:
        tab: liste dans laquelle chercher
        x: élément à rechercher
    
    Returns:
        int: indice de la première occurrence de x, ou -1 si absent
    """
    for i in range(len(tab)):
        if tab[i] == x:
            return i
    return -1


# Exemple d'utilisation
if __name__ == "__main__":
    # Test avec différents cas
    tableau1 = [1, 3, 5, 7, 9, 11]
    tableau2 = [2, 4, 6, 8, 10]
    tableau3 = []
    tableau4 = [5, 5, 5, 5]
    
    print("Test de la fonction recherche_lineaire:")
    print(f"recherche_lineaire({tableau1}, 5) = {recherche_lineaire(tableau1, 5)}")
    print(f"recherche_lineaire({tableau1}, 6) = {recherche_lineaire(tableau1, 6)}")
    print(f"recherche_lineaire({tableau2}, 8) = {recherche_lineaire(tableau2, 8)}")
    print(f"recherche_lineaire({tableau2}, 1) = {recherche_lineaire(tableau2, 1)}")
    print(f"recherche_lineaire({tableau3}, 1) = {recherche_lineaire(tableau3, 1)}")
    print(f"recherche_lineaire({tableau4}, 5) = {recherche_lineaire(tableau4, 5)}")
