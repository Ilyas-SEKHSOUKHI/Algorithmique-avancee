#Exercice 5
Prix_HT = [50,60,90,120]
Prix_TTC = []
for i in range(len(Prix_HT)):
    Prix_TTC.append(Prix_HT[i]-((Prix_HT[i]*20)/100))
print("Liste de prix HT : "+str(Prix_HT))
print("Liste de prix TTC : "+str(Prix_TTC))