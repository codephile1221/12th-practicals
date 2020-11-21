with open('Sentence.txt') as f:
    file_content = f.read().strip()
chars = [',','?','.','!']
for i in file_content:
    if i in chars:
        sentence = file_content.split(i)[0]
        print(sentence)
sentence = sentence.split(" ") 
for i in sentence:
    sum1 = 0
    for j in i:
        sum1 += ord(j)
    print(f'{i} : {sum1}')
sentence.sort()
for i in sentence:
    print(f"{i} ",end="")            