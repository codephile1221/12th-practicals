import datetime 
bikeid = [] 
out = [] 
while True:
    bikeid.append(input("Enter the ID "))
    out.append(float(input("Enter the time ")))
    print(bikeid)
    if bikeid[len(bikeid)-1] == 'ZZZ':
        break
check = input("Enter the ID to be checked")
if check  in bikeid:
    print(f'ID: {check}  OUT : {out[bikeid.index(check)]}')
    newtime = input('New time ')
    tdelta = datetime.datetime.strptime(newtime,'%H.%M')-datetime.datetime.strptime(str(out[bikeid.index(check)]),'%H.%M')
    print(f"Time difference is {tdelta}")
else:
    print('ID NOT FOUND')
