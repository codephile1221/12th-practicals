def BubbleSort(L):
    n=len(L)
    for i in range (n):
        for j in range (n-i-1):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    return L
n=int(input("enter size of list"))
List=[0]*n
for i in range (n):
    List[i]=int(input("enter element"+str(i)+":"))
print (List)
print("sorted list=", BubbleSort(List))
