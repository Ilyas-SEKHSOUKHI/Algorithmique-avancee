#Afficher la table de multiplication d’un nombre donné.
Number = int(input("Entrez un Nombre: "))
for i in range(10):
    Resultat = Number * i
    print(str(Number)+"x"+str(i)+"="+str(Resultat))