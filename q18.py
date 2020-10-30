l = []
top = 0
def add(l):
    global top
    bookno = int(input("enter the number of book here: "))
    bookname = input("enter book name here: ")
    cost = int(input("enter price of book here: "))
    temp = (bookno,bookname,cost)
    top += 1
    l.append(temp)

def display(l):
    for i in l:
        print(i, end = "")
    print()

def remove(l):
    if len(l) != 0:
        l.pop()
    else:
        print("underflow: list size is 0")

def size(l):
    return(top, ": size of the list")

print("1. add elements")
print("2. remove elements")
print("3. display elements")
print("4. show size")



while True:
    choice = int(input("enter numbered choice here: "))
    if choice == 1:
        add(l)
    elif choice == 2:
        remove(l)
    elif choice == 3:
        print(display(l))
    elif choice == 4:
        print(size(l))
    else:
        print("correct option not selected, terminating loop")
        break