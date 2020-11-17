def add_stud():
    a = open("student.txt", "w")
    roll_no = int(input("enter the roll no of the student here : "))
    name = input("enter the name of the student here : ")
    address = input("enter the address of the student here : ")
    record_list = [roll_no, name, address]
    a.write(record_list)

    a.close()

def disp_stud():
    a = open("student.txt", "r")
    if len(a) != 0:
        print(a.read())

    else:
        print("there is no information in the file")

def search_stud():
    a = open("student.txt", "r")
    rno = int(input("enter the roll no to be found : "))
    for i in a.readlines():
        if rno == i[0]:
            print(i, "student details")

print("adding a student's details")
print("displaying present student details")
print("searching for a student's details")
while True:
    choice = int(input("enter numbered choice here "))
    if choice == 1:
        add_stud()

    elif choice == 2:
        disp_stud()

    else: 
        search_stud()

    word = input("do you still wish to continue (Y/N) ")
    if word == "y" or word == "Y":
        continue
    else:
        break
