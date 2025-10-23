def tri_insertion(tab):
    for i in range(1, len(tab)):
        cle = tab[i]        # élément à insérer
        j = i - 1
        # Décale les éléments plus grands vers la droite
        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = cle     # place la clé à sa position correcte
