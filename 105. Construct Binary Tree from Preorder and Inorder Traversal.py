# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dict = {}
        length = len(preorder)
        for i in xrange(length):
            dict[inorder[i]] = i
        return self.build(preorder, dict, 0, length)
        
    def build(self, preorder, dict, pos, len):
        if len == 0:
            return None
        value = preorder[pos]
        root = TreeNode(value)
        inpos = dict[value]
        for i in xrange(pos+1, pos+len):
            if dict[preorder[i]] > inpos:
                root.left = self.build(preorder, dict, pos+1, i-pos-1)
                root.right = self.build(preorder, dict, i, len-i+pos)
                break
        else:
            root.left = self.build(preorder, dict, pos+1, len-1)
            root.right = None
        return root
        
        
        
        
        
        
        
        
        
        