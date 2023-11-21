class Node:
   def __init__(self, value):

       self.value = value
       self.left_child = None
       self.right_child = None

class BinarySearchTree:

   def __init__(self):
       self.root = None
   def insert(self, value):

       if self.root is None:
           self.root = Node(value)

       else:
           self._insert(value, self.root) 
   def _insert(self, value, current_node):

       if value < current_node.value:
           if current_node.left_child is None:
               current_node.left_child = Node(value)

           else:
               self._insert(value, current_node.left_child)
       elif value > current_node.value:
           if current_node.right_child is None:
               current_node.right_child = Node(value)
           else:
               self._insert(value, current_node.right_child)

       else:
           print("Value already exists in tree.")
   def search(self, value):
       if self.root is not None:
           return self._search(value, self.root)

       else:
           return False
   def _search(self, value, current_node):

       if value == current_node.value:
           return True

       elif value < current_node.value and current_node.left_child is not None:
           return self._search(value, current_node.left_child)

       elif value > current_node.value and current_node.right_child is not None:
           return self._search(value, current_node.right_child)

       else:
           return False


my_tree = BinarySearchTree()

my_tree.insert(1)
my_tree.insert(2)
my_tree.insert(3)

print(my_tree.search(3))


'''
# Python3 function to search a given key in a given BST

class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# A utility function to insert
# a new node with the given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # Return the (unchanged) node pointer
    return node

# Utility function to search a key in a BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root

    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

# Driver Code
if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    # Key to be found
    key = 6

    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")

    key = 60

    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")
'''