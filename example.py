from treecrypt import KeyMaker, Crypter
import os

try:
    open('keys/key.txt', 'r')
except FileNotFoundError:
    os.makedirs(os.path.dirname('keys/key.txt'), exist_ok=True)
    myKeyMaker = KeyMaker()
    myKeyMaker.GenerateKey(100, 5, livePrint=True)
    myKeyMaker.Export("keys/key.txt", "keys/dict.txt")


myCrypter = Crypter()
myCrypter.Import("keys/key.txt", "keys/dict.txt")
plainText = input("Enter text to encrypt: ")
cipher = myCrypter.Encrypt(plainText)
print(cipher)


cipher = input("Enter text to decrypt: ")
plainText = myCrypter.Decrypt(cipher)
print(plainText)