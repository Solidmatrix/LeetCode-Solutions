# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def robrob(self, root):
        if root == None:
            return [0, 0]
        l1, l2 = self.robrob(root.left)
        r1, r2 = self.robrob(root.right)
        return [root.val + l2 + r2, max(l1, l2) + max(r1, r2)]
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a, b = self.robrob(root)
        return max(a, b)
    
        