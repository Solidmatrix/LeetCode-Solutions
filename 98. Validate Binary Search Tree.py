# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isValid(root, -1-sys.maxint, sys.maxint)
    
    def isValid(self, root, ll, rr):
        if root.left:
            if root.left.val >= root.val or root.left.val <= ll or not self.isValid(root.left, ll, root.val):
                return False
        if root.right:
            if root.right.val <= root.val or root.right.val >= rr or not self.isValid(root.right, root.val, rr):
                return False
        return True
            
            
            