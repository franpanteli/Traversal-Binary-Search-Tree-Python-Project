"""
    Outline: 	
        -> We are defining a Binary Search Tree (BST) data structure 
        -> We are also setting up facilities to interact with this 
        -> These facilities are to insert, delete, search and perform inorder traversal 
            for this
        -> We define two classes for this (`TreeNode Class` and `BinarySearchTree`), and 
            then a block at the end of the .py file to test this  

    The `BinarySearchTree` class:
        -> This class has methods which allow us to manage the binary search tree 
        -> These methods let us manage nodes on the tree and perform an inorder traversal 
            -> To insert, delete and search for nodes 
"""

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)
    
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # This method adds a new node into the search tree. This node has a given key 
    def insert(self,key):
        self.root = self._insert(self.root, key)

    # This method is a helper function, which recursively inserts a node into the tree 
    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    # This method searches for a node with a given key in the tree
    def search(self, key):
        return self._search(self.root, key)

    # This is a helper function to recursively search for a node with a key in the tree
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # This `delete` method is for deleting nodes from the tree. The index of the node which 
        # is being deleted is the argument of this method 
    def delete(self, key):
        self.root = self._delete(self.root, key)

    # This is a helper function, to recursively delete a node from the tree 
    # The previous method was to delete a node from the tree -> this is what this helper function does 
    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)
        return node

    # This method is a helper function, to find the minimum value of a node in the subtree
    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    # This method performs an inorder traversal of the binary search tree
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    # This is a helper function which recursively performs the inorder traversal and stores the result 
        # of this in a list 
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

"""
    Code to define an instance of the class:
        -> This block of code creates an instance of the BinarySearchTree class
        -> We are inserting a list of nodes into the tree, printing the inorder traversal of this tree, searching for a specific 
            node, deleting this and then printing the inorder traversal again to see the changes 
"""

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)
print("Inorder traversal:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
bst.delete(40)
print("Inorder traversal after deleting 40:", bst.inorder_traversal())
print("Search for 40:", bst.search(40))
