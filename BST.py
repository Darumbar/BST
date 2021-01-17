# Pyton impelementation of a BST with insert, search and inorder functions

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with a given key

def insert(rootk, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root()
        elif root.val < key:
            root.right = insert(root.right, key)
        elif root.val > key:
            root.left = insert(root.right, key)
    return root

# A utility function to do inorder tree traversal

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# A utility function to search a given key in BST 
def search(root,key): 
      
    # Base Cases: root is null or key is present at root 
    if root is None or root.val == key: 
        return root 
  
    # Key is greater than root's key 
    if root.val < key: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key) 
