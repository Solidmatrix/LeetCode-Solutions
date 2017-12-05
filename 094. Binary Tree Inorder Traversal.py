# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        self.inorder(root, printlist)
        return printlist
    
    def inorder(self, root, printlist):
        if root != None:
            self.inorder(root.left, printlist)
            printlist.append(root.val)
            self.inorder(root.right, printlist)