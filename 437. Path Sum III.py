# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        count = 0
        stack = []
        stack.append(root)
        while len(stack) != 0:
            tmp = stack.pop()
            count += self.pathSum2(tmp, sum)
            if tmp.left != None:
                stack.append(tmp.left)
            if tmp.right != None:
                stack.append(tmp.right)
        return count
        
    def pathSum2(self, root, sum):
        if root == None:
            return 0
        result = self.pathSum2(root.left, sum-root.val) + self.pathSum2(root.right, sum-root.val)
        if root.val == sum:
            return 1 + result
        else:
            return result

        
        
        