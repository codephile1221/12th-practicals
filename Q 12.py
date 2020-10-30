#EXPT-12
def Count():
    f=open("coordinate.txt","r")
    count=0
    X=f.read()
    word=X.split()
    for I in word:
        if I.istitle()==True:
            count+=1
        else:
            continue
    print(count)  
Count()
    
    
