a = open("words.txt", "r")
temp_string = ""
b = open("word.txt", "w")
for i in a.read():
    if i == "j" or i == "J":
        temp_string += "i"
    else:
        temp_string += i
    
b.write(temp_string)
a.close()
b.close()