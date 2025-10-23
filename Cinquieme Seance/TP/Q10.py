def position_insertion(tab, x):
    """
    Fonction qui retourne la position où insérer x dans une liste triée
    pour maintenir l'ordre croissant.
    
    Args:
        tab: liste triée dans laquelle insérer
        x: élément à insérer
    
    Returns:
        int: position où insérer x pour maintenir l'ordre
    """
    gauche = 0
    droite = len(tab)
    
    while gauche < droite:
        milieu = (gauche + droite) // 2
        
        if tab[milieu] < x:
            gauche = milieu + 1
        else:
            droite = milieu
    
    return gauche


# Exemple d'utilisation
if __name__ == "__main__":
    # Test avec différents cas
    liste_triee1 = [1, 3, 5, 7, 9, 11]
    liste_triee2 = [2, 4, 6, 8, 10]
    liste_vide = []
    liste_un_element = [5]
    liste_dupliques = [1, 2, 2, 2, 3, 4, 5]
    
    print("Test de la fonction position_insertion:")
    print(f"position_insertion({liste_triee1}, 6) = {position_insertion(liste_triee1, 6)}")
    print(f"position_insertion({liste_triee1}, 0) = {position_insertion(liste_triee1, 0)}")
    print(f"position_insertion({liste_triee1}, 12) = {position_insertion(liste_triee1, 12)}")
    print(f"position_insertion({liste_triee2}, 7) = {position_insertion(liste_triee2, 7)}")
    print(f"position_insertion({liste_vide}, 5) = {position_insertion(liste_vide, 5)}")
    print(f"position_insertion({liste_un_element}, 3) = {position_insertion(liste_un_element, 3)}")
    print(f"position_insertion({liste_un_element}, 7) = {position_insertion(liste_un_element, 7)}")
    print(f"position_insertion({liste_dupliques}, 2) = {position_insertion(liste_dupliques, 2)}")
    
    # Démonstration de l'insertion
    print("\nDémonstration de l'insertion:")
    test_liste = [1, 3, 5, 7, 9]
    element_a_inserer = 6
    pos = position_insertion(test_liste, element_a_inserer)
    nouvelle_liste = test_liste[:pos] + [element_a_inserer] + test_liste[pos:]
    print(f"Liste originale: {test_liste}")
    print(f"Position d'insertion pour {element_a_inserer}: {pos}")
    print(f"Liste après insertion: {nouvelle_liste}")
