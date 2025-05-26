import random
import ast
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

    def Decrypt(self, string):
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
        
        words = string.split('|')
        out = ""
        for word in words:
            letters = word.split('.')
            for character in letters:
                realChar = decode(self, character)
                out = out + realChar
            out = out + " "
        out = out[:-1]
        return out
    
    def Encrypt(self, string):
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
            return BackTrace(self, parent, str)
        
        words = string.split(' ')
        out = ""
        for word in words:
            characters = list(word)
            for character in characters:
                trace = BackTrace(self, self.items[random.choice(self.dictionary[character])])
                out = out + trace + '.'
            out = out[:-1] + '|'
        out = out[:-1]
        return out

    def DrawKey(self):
        def draw_arrow(x1, y1, x2, y2):
            ax.annotate(
                '',
                xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5)
            )
        def PrepareGraph(self, ax, Root=None):
            if Root == None:
                Root = self.items[0]
            ellipse = patches.Ellipse((Root.x, Root.y), 0.5, 0.5, edgecolor='black', facecolor='lightblue')
            #ax.text(Root.x, Root.y, str(Root.index), ha='center', va='center', fontsize=6)
            ax.add_patch(ellipse)

            if Root.up:
                next = self.items[Root.up]
                draw_arrow(Root.x, Root.y + 0.2, next.x, next.y - 0.2)
                PrepareGraph(self, ax, next)
            if Root.left:
                next = self.items[Root.left]
                draw_arrow(Root.x - 0.2, Root.y, next.x + 0.2, next.y)
                PrepareGraph(self, ax, next)
            if Root.down:
                next = self.items[Root.down]
                draw_arrow(Root.x, Root.y - 0.2, next.x, next.y + 0.2)
                PrepareGraph(self, ax, next)
            if Root.right:
                next = self.items[Root.right]
                draw_arrow(Root.x + 0.2, Root.y, next.x - 0.2, next.y)
                PrepareGraph(self, ax, next)
        fig, ax = plt.subplots(figsize=(8, 8))
        PrepareGraph(self, ax)
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)
        ax.set_aspect('equal')
        plt.grid(True)
        plt.title("NODES")
        plt.show()
    
with open("key.txt", 'r', encoding='utf-8') as f:
    key = ast.literal_eval(f.readline())
with open("dict.txt", 'r', encoding='utf-8') as f:
    dictionary = ast.literal_eval(f.readline())

myCrypter = Crypter(key, dictionary)
myCrypter.DrawKey()
text = input("Enter text to encrypt: ")
cipher = myCrypter.Encrypt(text)
decrypted = myCrypter.Decrypt(cipher)

print(f"decrypted cipher (double check): \t{decrypted}")
print(f"cipher text: \t\t\t\t{cipher}")