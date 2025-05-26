import random
import ast

class Node:
    def __init__(self, x, y, index, ParentIndex):
        self.char = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.index = index
        self.parentIndex = ParentIndex
        self.x = x
        self.y = y
    
    def SetChar(self, char):
        self.char = char
    
    def getArray(self):
        return [self.x, self.y, self.up, self.left, self.down, self.right, self.char, self.index, self.parentIndex]

class Crypter:
    def __init__(self, key, dictionary):
        self.dictionary = dictionary
        self.items = []
        for nodeArray in key:
            newNode = Node(nodeArray[0], nodeArray[1], nodeArray[7], nodeArray[8])
            newNode.SetChar(nodeArray[6])
            newNode.up = nodeArray[2]
            newNode.left = nodeArray[3]
            newNode.down = nodeArray[4]
            newNode.right = nodeArray[5]
            self.items.append(newNode)
    
    def decode(self, string):
        trace = list(string)
        currentNode = self.items[0]
        for i in trace:
            match i:
                case 'u':
                    next = currentNode.up
                case 'l':
                    next = currentNode.left
                case 'd':
                    next = currentNode.down
                case 'r':
                    next = currentNode.right
            currentNode = self.items[next]
        return currentNode.char

    def Decrypt(self, string):
        words = string.split('|')
        out = ""
        for word in words:
            letters = word.split('.')
            for character in letters:
                realChar = self.decode(character)
                out = out + realChar
            out = out + " "
        out = out[:-1]
        return out
    
    def BackTrace(self, node, str=None):
        if node.parentIndex == None:
            return str
        if str == None:
            str = ""
        parent = self.items[node.parentIndex]
        if parent.up == node.index:
            str = 'u' + str
        if parent.left == node.index:
            str = 'l' + str
        if parent.down == node.index:
            str = 'd' + str
        if parent.right == node.index:
            str = 'r' + str
        return self.BackTrace(parent, str)
    
    def Encrypt(self, string):
        words = string.split(' ')
        out = ""
        for word in words:
            characters = list(word)
            for character in characters:
                trace = self.BackTrace(self.items[random.choice(self.dictionary[character])])
                out = out + trace + '.'
            out = out[:-1] + '|'
        out = out[:-1]
        return out
    
with open("key.txt", 'r', encoding='utf-8') as f:
    key = ast.literal_eval(f.readline())
with open("dict.txt", 'r', encoding='utf-8') as f:
    dictionary = ast.literal_eval(f.readline())

myCrypter = Crypter(key, dictionary)
text = input("Enter text to encrypt: ")
cipher = myCrypter.Encrypt(text)
decrypted = myCrypter.Decrypt(cipher)

print(f"plain text: \t{text}")
print(f"cipher text: \t{cipher}")
print(f"decrypted: \t{decrypted}")