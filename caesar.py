import string
alphabet = list(string.ascii_lowercase)
ende = raw_input("(1)Encrypt or (2)Decrypt ?\n>")
if ende == "1" or ende == "encrypt" or ende == "Encrypt":
    encrypt = True
else:
    encrypt = False
inp = raw_input("Type text:\n>")
empty = []
key = 13
key = int(raw_input("Enter shift key(default 13):\n>"))
for i in inp:
    for g in alphabet:
        if i == g:
            index = alphabet.index(g)
            if encrypt:
                if index + key >= 26:
                    total = index + key
                    count = 1 + total / 26
                    empty.append(alphabet[total - 26 * count])
                else:
                    a = index + key
                    empty.append(alphabet[a])
            else:
                if index + key >= 26:
                    total = index - key
                    count = 1 + total / 26
                    empty.append(alphabet[total - 26 * count])
                else:
                    a = index - key
                    empty.append(alphabet[a])


print ("Encrypted Text: " + ''.join(empty))
