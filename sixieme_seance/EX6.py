#Ex6 -Logarithmes imbriqués
m = n
while m > 0:
    t = m
    while t > 1:
        t = int(t**0.5)
    m //= 2
#Donnez une borne asymptotique serrée (indice: log n · log(log(n))).