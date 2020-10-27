#redacted program
def redacted_text(word, string):
    l = []
    l.append(word)
    final = ""
    string_value = string.split(" ")

    for i in string_value:
        if i in l:
            i = "REDACTED"
        final = final + (i + " ")

    return final

word = input("enter word to be redacted here: ")
string = input("enter sentence here: ")
print(redacted_text(word, string))
