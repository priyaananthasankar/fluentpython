# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val > high: # go left
            return rangeSumBST(root.left,low,high)
        elif root.val < low # go right
            return rangeSumBST(root.right,low,high)
        else:
            return root.val + rangeSumBST(root.left,low,root.val) + rangeSumBST(root.right,root.val,high)
            


