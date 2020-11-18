vip = []
balcony = []
regular = []
ref = {'h':vip ,'n':balcony,'l':regular }
command = ""
while command != '4':
    print('1.)Insert tokenID')
    print('2.)Search for an ID')
    print('3.)Change priority')
    print('4.)Quit')    
    command = input("Enter the choice ")
    if command == '1':
        tokenID = input("Enter tokenID ")
        priority = input("Enter priority ")
        if priority.lower() == 'h':
            vip.append(tokenID)
        elif priority.lower() == 'n':
            balcony.append(tokenID)
        elif priority.lower == 'l':
            regular.append(tokenID)
        else:
            print("Invalid Priority")
            continue
    elif command == '2':
        searchID = input("Enter the ID to be searched  ")
        m = [vip,balcony,regular,'vip','balcony','regular']
        found = False
        for i in m:
            for j in i:
                if j == searchID:
                    print(f"Element found in queue {m[m.index(i)+3]} at index {i.index(searchID)} ")
                    found = True
        if not found:
            print("ID not found ")
    elif command == '3':
        priority = input("Enter the priority of the tokenID to be changed  ")
        tokenID1 = input("Enter the tokenID of the priority you want to change ") 
        newpriority = input("Enter the new priority ") 
        print(newpriority)
        print(ref[priority])
        ref[priority].remove(tokenID1)
        if newpriority.lower() == 'h':
            vip.append(tokenID1)
        elif newpriority.lower() == 'n':
            balcony.append(tokenID1)
        elif newpriority.lower == 'l':
            regular.append(tokenID1)
    elif command == '4':
        break
    else:
        print("Invalid comamnd")
        continue