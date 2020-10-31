import sys
L=[]
N=int(input('Enter the length of list='))
print('Enter the numbers=')
for I in range(N):
    A=int(input())
    L.append(A)
print('List of numbers=',L)
def menu():
    while True:
        global L
        print('''MENU
1. Linear Search
2. Binary Search
3. Lowest Number
4. Selection Sort
5. EXIT''')
        ch=int(input('Enter your choice='))
        if ch==1:
            X=int(input('Enter the number to be searched='))
            INDEX=linearsearch(L,X)
            if INDEX or INDEX==0:
                print(f'Element {X} found at index postion : {INDEX}')
            else:
                print('Element not found')
        elif ch==2:
            print(sorted(L))
            X=int(input('Enter the number to be searched='))
            L.sort()
            INDEX=binarysearch(L,X)
            if INDEX or INDEX==0:
                print(f'Element {X} found at index postion : {INDEX}')
            else:
                print('Element not found')
        elif ch==3:
            print('Smallest number in the list is',lowestnumber(L))
        elif ch==4:
            selectionsort(L)
        elif ch==5:
            sys.exit()
    else:
        print('Invalid choice')
        sys.exit()

def linearsearch(L,X):
    for I in range(len(L)):
        if L[I]==X:
            return I

def binarysearch(L,X):
    beg=0
    last=len(L)-1
    while beg<=last:
        mid=(beg+last)//2
        if L[mid]==X:
            return mid
        else:
            if L[mid]>X:
                last=mid-1
            else:
                beg=mid+1
    else:
        return -1

def lowestnumber(L):
    small=L[0]
    for I in range(1,len(L)):
        if L[I]<small:
            small=L[I]
        else:
            pass
    return small
    
def selectionsort(L):
    for i in range(len(L)): 
        min_idx = i 
        for j in range(i+1, len(L)): 
            if L[min_idx] > L[j]: 
                min_idx = j         
            L[i],L[min_idx] = L[min_idx],L[i]
    print ("Sorted array")
    print(L)
 
menu()
    
            

