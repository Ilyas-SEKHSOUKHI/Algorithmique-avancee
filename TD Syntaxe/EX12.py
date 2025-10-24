# Calculer la moyenne des valeurs d’une liste donnée.
Liste = [1,2,3,4,5,6,7,8,9,10]
Somme = 0
for i in range(len(Liste)):
    Somme = Liste[i]+Somme
Moyenne = Somme/len(Liste)
print("Moyenne = ",Moyenne)