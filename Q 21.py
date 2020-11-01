#EXPT 21
C='y'
MAJL=[]
def itemnode(entry):
    if entry=="Ins":
        A='yes'
        while A=='yes':
            MINL=[]
            MNo=int(input("Enter the member no.="))
            MName=str(input("Enter member name-"))
            Age=int(input("Enter member age="))
            MINL.append(MNo)
            MINL.append(MName)
            MINL.append(Age)
            MAJL.append(MINL)
            A=input("If you wish to continue with inserting data enter 'yes':")
        print(MAJL)
    elif entry=="Del":
        if len(MAJL)==0:
            print("queue is empty")
        else:
            MAJL.pop(0)
            print(MAJL)
while C=='y':
    entry=str(input("Do you wish to input data or delete data? For former enter 'Ins' and for latter enter 'Del:"))
    itemnode(entry)
    C=input("Do you wish to continue with the program:")        
            
        
            
        
