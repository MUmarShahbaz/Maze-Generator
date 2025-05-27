from treecrypt import KeyMaker, Crypter

try:
    open('keys/key.txt', 'r')
except FileNotFoundError:
    CustomCharset = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', "'", ',', '.', '?', '/'
        ]
    myKeyMaker = KeyMaker(CustomCharset)
    myKeyMaker.GenerateKey(20, 5)
    myKeyMaker.Export("keys/key.txt", "keys/dict.txt")


myCrypter = Crypter()
myCrypter.Import("keys/key.txt", "keys/dict.txt")
#myCrypter.DrawKey()

plainText = input("Enter text to encrypt: ")
cipher = myCrypter.Encrypt(plainText)
print(cipher)


cipher = input("Enter text to decrypt: ")
plainText = myCrypter.Decrypt(cipher)
print(plainText)