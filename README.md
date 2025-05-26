# TreeCrypt
## Node-Tree based encryption algorithm

### Basic Working
- Code creates a random tree of nodes
- Each node contains a character, multiple nodes can contain the same character
- Each character in the input is converted into a trace of a node which stores the same character
- The trace shows how to reach the node with the character from the root node

### Tree Ruleset
- There will be a Root Node
- There will be a max-depth
- Each node will point to 3 other nodes who will be a random distance away
- When mapped onto a 2D Plane, no node or edge will intersect with anything else
- Depending on how cramped a node is, it may not point to any other even though the max-depth hasn't been reached
- It can be plotted as a 2D Graph. This is actually an option.

### KeyMaker Parameters
- charset :  
  A set of characters that will be encrypted. The input string must contain only these characters or spaces. There is only one rule on the charset. It must be a single char and it must be one which can be stored as a key in a dictionary.
- depth:  
  The maximum number of nodes away from the root that a node can be. The code will try to get as many nodes to reach max-depth as possible
- MaxDist:  
  The maximum distance between 2 connected nodes

### KeyMaker Outputs
- key.txt:  
  The tree itself
- dict.txt:
  A dictionary which is useless without the key, unique to the key and only serves to speed up the encryption purpose.

### KeyMaker Functions

- GetKey(): Returns an array of arrays which is the key
- GetDictionary(): Returns a dictionary which is used to speed up encryption progress
- GenerateKey(): Generates a random key and dictionary
- DrawKey(): Creates a graphical representation of the key

### Crypter Functions

- Encrypt(): Converts a string to a cipher
- Decrypt(): Reverts ciphers to the plain text
- DrawKey(): Creates a graphical representation of the key