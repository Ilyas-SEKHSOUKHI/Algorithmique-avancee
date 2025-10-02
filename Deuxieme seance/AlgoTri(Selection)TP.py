List=[5,1,2,36]
for i in range(len(List)):
    min = i
    for j in range(i+1,len(List)):
        if(List[j]<List[min]):
            min = j
    List[i],List[min]=List[min],List[i]
print(List)