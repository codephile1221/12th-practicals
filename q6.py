import sys
def copy(S,P=''):
    if len(S)==0:
        return P
    else:
        P=P+S[0]
        return P + copy(S[1:])
        
S=input('Enter string = ')
P=''
print('Original string is = ',S)
print('String copied into another variable is = ',copy(S,P))

