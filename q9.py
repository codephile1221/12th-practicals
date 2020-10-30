def pattern(n):
    s=str(n)+','
    m=n
    if n>0:
        while n>0:
            n=n-5
            s=s+str(n)+','
    if n<=0:
        while n!=m:
            n=n+5
            s=s+str(n)+','
    print(s)
N=int(input('Enter number required for the pattern = '))
print('Pattern = ')
pattern(N)
      
