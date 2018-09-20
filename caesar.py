alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ende = raw_input("(1)Encrypt or (2)Decrypt ?\n>")
if ende == "1" or ende == "encrypt" or ende == "Encrypt":
    encrypt = True
else:
    encrypt = False
inp = raw_input("Type text:\n>")
empty = []
key = 13
try:
    key = int(raw_input("Enter shift key(default 13):\n>"))
except:
    pass
for i in inp:
    for g in alphabet:
        if i == g:
            index = alphabet.index(g)
            if encrypt:
                a = index + key
            else:
                a = index - key
            empty.append(alphabet[a])


print ("Encrypted Text: " + ''.join(empty))
