import string
clave = 'VCHPRZGJNTLSKFBDQWAXEUYMOI'
alfabeto = string.ascii_uppercase
plaintext = input('DIGITE UNA PALABRA : ')
ciphertext = ''
for plaintext in plaintext.upper():
    for a in alfabeto:
        if plaintext ==a:
            ciphertext += clave[alfabeto.index(plaintext)]
print(ciphertext) 