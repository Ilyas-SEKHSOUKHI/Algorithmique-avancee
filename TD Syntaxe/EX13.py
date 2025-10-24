#Écrire un programme qui renvoie le plus grand et le plus petit élément d’une liste.
def Plus_Grande(Liste):
    for i in range(len(Liste)):
        max = i
        for j in range(i+1,len(Liste)):
            if Liste[j] > Liste[max]:
                max = j
        temp = Liste[i]
        Liste[i] = Liste[max]
        Liste[max] = temp
    print(Liste[0])

def Plus_Petit(Liste):
    for i in range(len(Liste)):
        min = i
        for j in range(i+1,len(Liste)):
            if Liste[j] < Liste[min]:
                min = j
        temp = Liste[i]
        Liste[i] = Liste[min]
        Liste[min] = temp
    print(Liste[0])

Liste = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
Plus_Grande(Liste)
Plus_Petit(Liste)