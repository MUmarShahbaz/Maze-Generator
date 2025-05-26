import random
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
    
class KeyMaker:
    def __init__(self, charset):
        self.items = [Node(0, 0, 0, None)]
        self.used = [[0, 0]]
        self.chars = charset
        self.dictionary = {char: [] for char in self.chars}
    
    def GetKey(self):
        key = []
        for node in self.items:
            key.append(node.getArray())
        return key
    
    def GetDictionary(self):
        return self.dictionary
        
    def GenerateKey(self, Depth, MaxDist, MinDist=1):
        def AttachLevels(self, node, level, start, MinDist, MaxDist):
            def AttachRandom(self, AttachToNODE, MaxDist, MinDist=1, tries=20):
                while True:
                    choices = ['u', 'l', 'd', 'r']
                    random.shuffle(choices)
                    dir = random.choice(choices)
                    dist = random.randrange(MinDist, MaxDist)
                    match dir:
                        case 'u':
                            x = AttachToNODE.x
                            y = AttachToNODE.y + dist
                            newUsed = []
                            for i in range(1, dist):
                                newUsed.append([AttachToNODE.x, AttachToNODE.y + i])
                        case 'l':
                            x = AttachToNODE.x - dist
                            y = AttachToNODE.y
                            newUsed = []
                            for i in range(1, dist):
                                newUsed.append([AttachToNODE.x - i, AttachToNODE.y])
                        case 'd':
                            x = AttachToNODE.x
                            y = AttachToNODE.y - dist
                            newUsed = []
                            for i in range(1, dist):
                                newUsed.append([AttachToNODE.x, AttachToNODE.y - i])
                        case 'r':
                            x = AttachToNODE.x + dist
                            y = AttachToNODE.y
                            newUsed = []
                            for i in range(1, dist):
                                newUsed.append([AttachToNODE.x + i, AttachToNODE.y])
                    flag = False
                    for node in self.items:
                        # Check if node already in place
                        if node.x == x and node.y == y:
                            flag = True
                        
                        # Check if new node passes over an old node
                        for newUsedX, newUsedY in newUsed:
                            if node.x == newUsedX and node.y == newUsedY:
                                flag = True
                    
                    for usedX, usedY in self.used:
                        # Check if an old node passes over the new node
                        if usedX == x and usedY == y:
                            flag = True
                        
                        # Check if the path of new node intersects path of an old node
                        for newUsedX, newUsedY in newUsed:
                            if usedX == newUsedX and usedY == newUsedY:
                                flag = True
                    if flag == False:
                        break
                    tries = tries - 1
                    if tries == 0:
                        return
                free = len(self.items)
                match dir:
                    case 'u':
                        AttachToNODE.up = free
                    case 'l':
                        AttachToNODE.left = free
                    case 'd':
                        AttachToNODE.down = free
                    case 'r':
                        AttachToNODE.right = free
                character = random.choice(self.chars)
                self.items.append(Node(x, y, free, AttachToNODE.index))
                self.items[free].SetChar(character)
                self.dictionary[character].append(free)
                self.used.extend(newUsed)
                print(len(self.items))

            if start == level:
                return
            AttachRandom(self, node, MaxDist, MinDist)
            AttachRandom(self, node, MaxDist, MinDist)
            AttachRandom(self, node, MaxDist, MinDist)
            if node.up:
                AttachLevels(self, self.items[node.up], level, start + 1, MinDist, MaxDist)
            if node.left:
                AttachLevels(self, self.items[node.left], level, start + 1, MinDist, MaxDist)
            if node.down:
                AttachLevels(self, self.items[node.down], level, start + 1, MinDist, MaxDist)
            if node.right:
                AttachLevels(self, self.items[node.right], level, start + 1, MinDist, MaxDist)
        self.items = [Node(0, 0, 0, None)]
        self.used = [[0, 0]]
        self.dictionary = {char: [] for char in self.chars}
        AttachLevels(self, self.items[0], Depth, 0, MinDist, MaxDist)
    
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

charset = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', ':', ';', '"', ',', '.', '?', '/'
]

myEnc = KeyMaker(charset)
myEnc.GenerateKey(20, 5)
with open("key.txt", 'w', encoding='utf-8') as f:
    f.write(f"{myEnc.GetKey()}")
with open("dict.txt", 'w', encoding='utf-8') as f:
    f.write(f"{myEnc.GetDictionary()}")