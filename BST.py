# Pyton impelementation of a BST with insert, search and inorder functions

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# A utility function to insert a new node with a given key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root()
        elif root.val < key:
            root.right = insert(root.right, key)
        elif root.val > key:
            root.left = insert(root.left, key)
    return root

# A utility function to do inorder tree traversal

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
# A utility function to do reverse order tree traversal

def revorder(root):
    if root:
        revorder(root.right)
        print(root.val)
        revorder(root.left)
        
# A utility function to do pre order traversal

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

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

# Driver program to test the above functions 
# Let us create the following BST 
#     50 
#   /     \ 
#  30     70 
#  / \    / \ 
# 20 40  60 80 

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

print("In order traversal")
inorder(r)
print("")
print("Reverse order traversal")
revorder(r)
print("")
print("Pre-order traversal")
preorder(r)