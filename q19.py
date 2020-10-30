#writing content to the file
file = open("words.txt", "a")
n = int(input("how many lines do you want to add to the file: "))
for i in range(n):
    choice = input("enter choice of words here: ")
    file.write(choice + "\n")
file.close()

#displaying all the content from the file using stack implementation
truh = open("words.txt", "r")
a = truh.readlines()
for i in range(len(a)-1,-1,-1):
    print(a[i])
truh.close()