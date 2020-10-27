#caesar cipher
def caesar_cipher(word, shift):
    new = []
    for i in word:
        encrypted_char = ord(i) + shift
        new.append(encrypted_char)
    final = ""
    for letter in new:
        final += chr(letter)
    return final

choice = input()
number = int(input())
print(caesar_cipher(choice, number))
