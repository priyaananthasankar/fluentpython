class TreeNode:
    def __init__(self,data=0,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def height_tree(self,root):
        if root == None:
            return 0
        lheight = self.height_tree(root.left)
        rheight = self.height_tree(root.right)
        depth = max(lheight,rheight) + 1

        return depth

obj = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)

print(obj.height_tree(root))
