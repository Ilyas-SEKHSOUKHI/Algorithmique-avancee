#Afficher une liste à l’envers sans utiliser reverse().
Liste = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(Liste)):
    print(Liste[len(Liste)-1-i])