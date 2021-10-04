############################################################
########### Depth First Tree Traversals via recursion ######
############################################################
class TreeNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

# Inorder traversal
def inorder_traverse(root):
    if root != None:
        inorder_traverse(root.left)
        print(root.data)
        inorder_traverse(root.right)
    else:
        return

# Preorder traversal
def preorder_traverse(root):
    if root != None:
        print(root.data)
        inorder_traverse(root.left)
        inorder_traverse(root.right)
    else:
        return

# Postorder traversal
def postorder_traverse(root):
    if root != None: 
        inorder_traverse(root.left)
        inorder_traverse(root.right)
        print(root.data)
    else:
        return

def populate_tree():
    left = TreeNode(1,None,None)
    right = TreeNode(3,None,None)
    root = TreeNode(2,left,right)
    return root

test_root = populate_tree()
print("Inorder traverse")
inorder_traverse(test_root)
print("Preorder traverse")
preorder_traverse(test_root)
print("Postorder traverse")
postorder_traverse(test_root)