choice = input("PLease enter the string choice here: ")
characters = [",", "?","!","."]
if choice[len(choice)-1] in characters:
    words = choice.split(" ")
    a = words[len(words)-1]
    final = ""
    for i in range(len(a)):
        if a[i] not in characters:
            final += a[i]
    words.pop()
    words.append(final)
    words.sort()
    for i in range(len(words)):
        print(words[i], end = " ")
else:
    print("Enter the correct end of line character")

