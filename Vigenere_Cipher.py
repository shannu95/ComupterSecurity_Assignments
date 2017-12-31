dict = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',',','.','-','_']
def Encryption(ptext, used_key):
    cipher = ''
    for i in range(len(ptext)):
        index = dict.index(ptext[i]) + dict.index(used_key[i])
        c = dict[index % len(dict)]
        cipher += c
    return cipher
plaintext = input('Enter the Plaintext: ').upper()
key = input('Enter the Key: ').upper()
ciphertext = ''
PTextblock = []

if len(key) < len(plaintext):
    for i in range(0, len(plaintext), len(key)):
        PTextblock.append((plaintext[i:i + len(key)]))
else:
    PTextblock.append(plaintext)

for plain in PTextblock:
    key = Encryption(plain, key)
    ciphertext += key
print('The Ciphertext is :', ciphertext)
