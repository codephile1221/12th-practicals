def add_stud():
    a = open("student.txt", "w")
    roll_no = int(input("enter the roll no of the student here : "))
    name = input("enter the name of the student here : ")
    address = input("enter the address of the student here : ")
    temp = (str(roll_no) + "," + name + "," + address + "\n")
    a.write(temp)
    a.close()

def disp_stud():
    a = open("student.txt", "r")
    b = a.read()
    if len(b) != 0:
        return b

    else:
        print("there is no information in the file")

def search_stud():
    temp_string = ""
    a = open("student.txt", "r")
    rno = input("Please enter roll no to be searched : ")
    for i in a.readlines():
        for k in i.split(","):
            if rno == k[0:2]:
                temp_string += i
    return temp_string

print("1 adding a student's details\n ")
print("2 displaying present student details\n ")
print("3 searching for a student's details\n")
while True:
    choice = int(input("enter numbered choice here "))
    if choice == 1:
        add_stud()

    elif choice == 2:
        print(disp_stud())

    else: 
        print(search_stud())

    word = input("do you still wish to continue (Y/N) ")
    if word == "y" or word == "Y":
        continue
    else:
        break
