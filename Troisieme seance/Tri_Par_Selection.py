#Premier Type de Tri
print("--------------Tri Par Selection--------------")
def Tri_Selection(tab):
    for i in range(len(tab)): # Parcourt chaque élément du tableau
        min = i # On suppose que la première valeur non triée est la plus petite
        for j in range(i+1,len(tab)): # On cherche la plus petite valeur dans le reste du tableau
            if tab[j]<tab[min]: # Si on trouve un élément plus petit que celui à la position min
                min = j  # On met à jour la position du minimum
        # Une fois le plus petit élément trouvé, on l'échange avec la position i
        temp = tab[i]
        tab[i]=tab[min]
        tab[min]=temp
    return tab  # On retourne le tableau trié

liste = [5,1,2,4,8,9,10]
print(Tri_Selection(liste))