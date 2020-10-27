#pig latin
def piglatin(s):
    l = []
    new = ""
    n = len(s)
    if s[n-1] == "y" and s[n-2] == "a":
        for i in s:
            l.append(i)

        l.pop()
        l.pop()

        for i in l:
            new += i

        final = l.pop()
        return(final + new[0:len(new)-1])

word = input()
print(piglatin(word))

