def tri_selection(tab):
    n = len(tab)
    for i in range(n - 1):
        # Trouver l'indice du plus petit élément à partir de i
        min_index = i
        for j in range(i + 1, n):
            if tab[j] < tab[min_index]:
                min_index = j
        # Échanger le plus petit élément trouvé avec tab[i]
        tab[i], tab[min_index] = tab[min_index], tab[i]
