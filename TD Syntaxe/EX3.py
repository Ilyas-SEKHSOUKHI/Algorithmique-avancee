#Lire un nombre et afficher sa nature.
nombre = int(input("Entrez un nombre : "))
if nombre>0:
    print(str(nombre) + " est > 0") 
elif nombre<0:
    print(str(nombre) + " est < 0")
else:
    print("null")


