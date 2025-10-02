liste = [4,3,6,5,7,8,9]
for i in range(1, len(liste)):
    key = liste[i]  
    j = i - 1
    while j >= 0 and liste[j] > key:
        liste[j+1] = liste[j]
        j -= 1
    liste[j+1] = key

print(liste)
