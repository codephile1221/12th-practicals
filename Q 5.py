#
PLANE=[]
DUE=[]
CALL=[]
C='y'
def inputer():
    while True:
        P=str(input("enter the plane id:"))
        PLANE.append(P)
        if P=="ZZZ":
            break
        D=int(input("enter take off time:"))
        DUE.append(D)
        C=int(input("enter calling time:"))
        CALL.append(C)
        
def identifier():
    if PLANE==[] or PLANE==['ZZZ'] or PLANE[0]="ZZZ":
        print("there are no planes waiting")
    else:
        print("next plane is ",PLANE[0],"due",DUE[0],'calling',CALL[0])
        PLANE.pop(0)
        DUE.pop(0)
        CALL.pop(0)
        L=len(PLANE)
        print("there are",L,"planes left for take off")
while C=='y':
    APP=str(input("Do you wish to input plane data or find the next plane for take? For former enter D and for latter enter T:"))
    if APP=="D":
        inputer()
    elif APP=="T":
        identifier()
    else:
        print("wrong input")
    C=input("Do u wish to continue with the program:")
    
    
        
    
    
