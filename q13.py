def group_ascii(a):
    sum = 0 
    for i in a:
        sum += ord(i)
    return sum

choice = input("please enter your string choice here : ")
characters = [',','?','.','!']
if choice[len(choice)-1] in characters:
    words = choice.split(" ")
    last = words[len(words)-1]
    temp_string = ""
    for l in last:
        if l.isalpha():
            temp_string += l
    words.pop()
    words.append(temp_string)

    temp_list = []
    for t in words:
        a = group_ascii(t)
        temp_list.append(a)
    
    temp_list.sort()
    
    for number in temp_list:
        for word in words:
            if group_ascii(word) == number:
                print(word, end = " ")

else:
    print("invalid character, please enter the correct end of line character")
    