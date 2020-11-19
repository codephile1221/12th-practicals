#25
C='y'
D={1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII' , 9:'IX', 10:'X'}
while C=='y':
    def addno():
        import pickle
        D={}
        L=10
        for I in range(L):
            F=open("Roman numeral.txt",'wb+')
            number=int(input("Enter a number:"))
            roman=str(input("Enter roman numeral of the entered number:"))
            D[number]=roman
        print(D)
        pickle.dump(D,F)
        F.close()
    def getno():
        import pickle
        F=open("Roman numeral.txt",'rb+')
        try:
            while True:
                R=pickle.load(F)
                A=int(input("Enter number whose roman equivalent is required:"))
                for X in R:
                    print(X)
                    if A==X:
                        print("Roman equivalent of " , A , "is" , R[X])
                        F.close()
                        return
        except EOFError:
            print("Number does not exist in dictionary")
            F.close()
    Entry=str(input("do u wish create dictionary(enter add) or search for roman equivalent(enter get):"))
    if Entry=='add':
        addno()
    elif Entry=='get':
        getno()
    C=input("if you wish to continue to continue program enter 'y' :")
    
    
    
    


                    
                    
        
