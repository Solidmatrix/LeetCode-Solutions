# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameter(self, root):
        if root == None:
            return [0, 0]
        [ll, lll] = self.diameter(root.left)
        [rr, rrr] = self.diameter(root.right)
        return [max(ll, rr) + 1, max(ll+rr+1, lll, rrr)]
            
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        [ll, lll] = self.diameter(root.left)
        [rr, rrr] = self.diameter(root.right)
        return max(ll+rr+1, lll, rrr) - 1
        
        
        