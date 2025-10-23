def recherche_dichotomique(tab, x):
    """
    Fonction qui effectue une recherche binaire de x dans un tableau trié.
    Retourne l'indice de x s'il est trouvé, ou -1 s'il est absent.
    
    Args:
        tab: liste triée dans laquelle chercher
        x: élément à rechercher
    
    Returns:
        int: indice de x s'il est trouvé, ou -1 s'il est absent
    """
    gauche = 0
    droite = len(tab) - 1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        
        if tab[milieu] == x:
            return milieu
        elif tab[milieu] < x:
            gauche = milieu + 1
        else:  # tab[milieu] > x
            droite = milieu - 1
    
    return -1


# Exemple d'utilisation
if __name__ == "__main__":
    # Test avec différents cas
    tableau_trie1 = [1, 3, 5, 7, 9, 11, 13, 15]
    tableau_trie2 = [2, 4, 6, 8, 10, 12]
    tableau_vide = []
    tableau_un_element = [5]
    tableau_dupliques = [1, 2, 2, 2, 3, 4, 5]
    
    print("Test de la fonction recherche_dichotomique:")
    print(f"recherche_dichotomique({tableau_trie1}, 7) = {recherche_dichotomique(tableau_trie1, 7)}")
    print(f"recherche_dichotomique({tableau_trie1}, 6) = {recherche_dichotomique(tableau_trie1, 6)}")
    print(f"recherche_dichotomique({tableau_trie2}, 8) = {recherche_dichotomique(tableau_trie2, 8)}")
    print(f"recherche_dichotomique({tableau_trie2}, 1) = {recherche_dichotomique(tableau_trie2, 1)}")
    print(f"recherche_dichotomique({tableau_vide}, 1) = {recherche_dichotomique(tableau_vide, 1)}")
    print(f"recherche_dichotomique({tableau_un_element}, 5) = {recherche_dichotomique(tableau_un_element, 5)}")
    print(f"recherche_dichotomique({tableau_un_element}, 3) = {recherche_dichotomique(tableau_un_element, 3)}")
    print(f"recherche_dichotomique({tableau_dupliques}, 2) = {recherche_dichotomique(tableau_dupliques, 2)}")
