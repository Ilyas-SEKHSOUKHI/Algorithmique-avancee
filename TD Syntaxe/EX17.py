#Calculer la factorielle d’un nombre avec une fonction.
'''
def factorielle(Number):
    Resultat = 1
    for i in range(1,Number+1):
        Resultat = Resultat*i
    return Resultat
'''

def factorielle(n):
    # Cas de base : quand n atteint 0 ou 1
    if n == 0 or n == 1:
        return 1
    else:
        # Appel récursif : la fonction s'appelle elle-même
        return n * factorielle(n - 1)

Number = int(input("Entrez un nombre : "))
print(factorielle(Number))



