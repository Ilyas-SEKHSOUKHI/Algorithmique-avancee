#Deuxieme type de tri
print("--------------Tri Par Insertion--------------")
def tri_insertion(tab):                     # Définition de la fonction tri_insertion qui prend une liste 'tab'
    for i in range(1, len(tab)):            # On parcourt la liste à partir du 2e élément (index 1)
        element = tab[i]                    # On garde l'élément courant à insérer dans la partie triée
        j = i - 1                           # On commence la comparaison avec l'élément précédent
        # Tant qu'on n'est pas au début et que l'élément précédent est plus grand que celui à insérer
        while j >= 0 and tab[j] > element:
            tab[j + 1] = tab[j]             # On décale l'élément vers la droite pour faire de la place
            j -= 1                          # On recule dans la liste pour continuer à comparer
        tab[j + 1] = element                # On insère l'élément à sa bonne position
    return tab                              # On retourne la liste triée

# Exemple d'utilisation :
liste = [5, 2, 4, 6, 1, 3]                  # On crée une liste non triée
print("Avant le tri :", liste)              # Affiche la liste avant le tri
print("Après le tri  :", tri_insertion(liste))  # Affiche la liste après le tri
