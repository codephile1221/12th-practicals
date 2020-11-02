def Bsearch(arr, start, end, x):
    if end >= start:
      mid = start + (end- start)//2
      if arr[mid] == x:
          return mid
      elif arr[mid] > x:
          return Bsearch(arr, start, mid-1, x)
      else:
          return Bsearch(arr, mid+1, end, x)
    else:
        return -1     
n=int(input("enter size"))
L=[0]*n
for i in range (n):
    L[i]=int(input("enter element"+str(i)+":"))
print(L)
item=int(input("enter item to be located"))
index=Bsearch(L, 0, len(L)-1, item)
if index!=-1:
    print("element found at index",index,"position",(index+1))
else:
    print("element not found")
