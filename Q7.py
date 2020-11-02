def Bsearch(list,x):
    beg=0
    last=len(list)-1
    while beg<=last:
        mid=(beg+last)//2
        if list[mid]==x:
            return mid
        else:
            if list[mid]>x:
                last=mid-1
            else:
                beg=mid+1
    return -1
n=int(input("enter size"))
L=[0]*n
for i in range (n):
    L[i]=int(input("enter element"+str(i)+":"))
print(L)
item=int(input("enter item to be located"))
index=Bsearch(L,item)
if index!=-1:
    print("element found at index",index,"position",(index+1))
else:
    print("element not found")
