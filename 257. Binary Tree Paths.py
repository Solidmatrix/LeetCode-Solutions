# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        if len(left) == len(right) == 0:
            return [str(root.val)]
        result = []
        val = str(root.val)+"->"
        for s in left:
            result.append(val + s)
        for s in right:
            result.append(val + s)
        return result