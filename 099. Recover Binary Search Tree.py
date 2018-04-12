# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        self.node1 = None
        self.node2 = None
        self.lastNode = None
        self.flag = False
        
        self.preorder(root)

        a = self.node1.val
        self.node1.val = self.node2.val
        self.node2.val = a
        return 

    def preorder(self, root):
        if root == None or self.flag:
            return
        self.preorder(root.left)
        if self.lastNode == None:
            self.lastNode = root
            self.preorder(root.right)
            return
        val = root.val
        if self.node1 == None and val < self.lastNode.val :
            self.node1 = self.lastNode
            self.node2 = root
        elif self.node1 != None and val < self.lastNode.val:
            self.node2 = root
            self.flag = True
            return
        self.lastNode = root
        self.preorder(root.right)
        