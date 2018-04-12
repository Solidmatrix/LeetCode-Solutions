# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convert(self, root, v):
        if root == None:
            return v
        rr = self.convert(root.right, v)
        root.val += rr
        return self.convert(root.left, root.val)
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.convert(root, 0)
        return root