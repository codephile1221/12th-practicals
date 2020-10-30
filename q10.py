import sys
def multiplication(N,i=1):
    print(N,'*',i,"=",N*i)
    if i<10:
        i+=1
    else:
        sys.exit()
    multiplication(N,i)
N=int(input('Enter a number = '))
multiplication(N)
    
