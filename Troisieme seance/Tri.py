#Tri par selection
'''print("Tri par selection")
def Tri_Par_Selection(Tab):
    for i in range(len(Tab)):
        min = i 
        for j in range(i+1,len(Tab)):
            if Tab[j]<Tab[min]:
                min = j
        temp = Tab[i]
        Tab[i]=Tab[min]
        Tab[min]=temp      
    return Tab '''
#Tri par Insertion
'''print("Tri par Insertion")
def Tri_par_Insertion(Tab):
    for i in range(1,len(Tab)):
        element = Tab[i]
        j = i-1
        while j>=0 and Tab[j]>element:
            Tab[j+1]=Tab[j]
            j-=1
        Tab[j+1]=element
    return Tab'''

liste = [5,2,1,4,7,6,9]
print(Tri_par_Insertion(liste))