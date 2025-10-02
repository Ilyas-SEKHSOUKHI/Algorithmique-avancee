def selection_sort(tab):
    n = len(tab)
    for i in range(n):
        # On suppose que la plus petite valeur est à la position i
        min_index = i
        for j in range(i+1, n):
            if tab[j] < tab[min_index]:
                min_index = j
        # Échanger l’élément minimum trouvé avec l’élément à la position i
        tab[i], tab[min_index] = tab[min_index], tab[i]
    return tab

# Exemple d’utilisation
liste = [64, 25, 12, 22, 11]
print("Avant tri :", liste)
print("Après tri :", selection_sort(liste))


#Cree par ChatGPT A Reviser