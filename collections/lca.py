class TreeNode:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

# Logic: 
# - Lowest common ancestor of the root node is root itself
# - Lowest common ancestor of two nodes on the same subtree is the root of the subtree
# - Using the above intuition check if n1 and n2 lie on different subtrees, if so return root
# - Else return node of that specific subtree where it was found
class Solution:
    def lca(self,root,n1,n2):
        if root == None:
            return None
        if root.data == n1 or root.data == n2:
            return root
        lnode = self.lca(root.left,n1,n2)
        rnode = self.lca(root.right,n1,n2)
        if lnode != None and rnode != None:
            return root
        if lnode != None:
            return lnode
        else:
            return rnode

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)

print(obj.lca(root,2,5).data)
print(obj.lca(root,2,3).data)
print(obj.lca(root,4,5).data)