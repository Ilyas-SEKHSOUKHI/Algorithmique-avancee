#Demander deux nombres et une opération (+, -, ×, ÷) et calculer le résultat.
def div(Numbre_1,Numbre_2):
    while Numbre_2==0:
        Numbre_2 = int(input("Entrez un Nombre: "))
    Div= Numbre_1/Numbre_2
    print("Div : "+str(Div))


Numbre_1 = int(input("Entrez un Nombre: "))
Numbre_2 = int(input("Entrez un Nombre: "))
Opp = input("Entrez une operation: ")

if Opp=="+":
    Somme = Numbre_1+Numbre_2
    print("La Somme : "+str(Somme))
elif Opp=="-":
    soustraction = Numbre_1-Numbre_2
    print("Soustraction : "+str(soustraction))
elif Opp=="*":
    Mult= Numbre_1*Numbre_2
    print("La Multiplication : "+str(Mult))
elif Opp=="/" or Opp=="÷":
    div(Numbre_1,Numbre_2)
else:
    print("Euror")