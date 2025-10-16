stock = {"stylo":10,"cahier":5}
article = input("Entrez le nom d'article : ")
Quatite = int(input("Entrez la valeur : "))
if article not in stock:
    stock[article]=0
else:
    stock[article]-=Quatite
print(stock)