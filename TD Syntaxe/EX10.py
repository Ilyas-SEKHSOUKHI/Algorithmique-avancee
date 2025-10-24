#Calculer la somme des éléments d’une liste sans sum().
Liste = [1,2,3,4,5,6,7,8,9,10]
Somme = 0
for i in range(len(Liste)):
    Somme = Liste[i]+Somme
print(Somme)