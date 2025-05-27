from treecrypt import KeyMaker, Crypter

try:
    open('keys/key.txt', 'r')
except FileNotFoundError:
    myKeyMaker = KeyMaker()
    myKeyMaker.GenerateKey(20, 5)
    myKeyMaker.Export("keys/key.txt", "keys/dict.txt")


myCrypter = Crypter()
myCrypter.Import("keys/key.txt", "keys/dict.txt")

plainText = input("Enter text to encrypt: ")
cipher = myCrypter.Encrypt(plainText)
print(cipher)


cipher = input("Enter text to decrypt: ")
plainText = myCrypter.Decrypt(cipher)
print(plainText)