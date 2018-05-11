# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if root == None:
            return []
        queue = [[]]
        queue[-1].append(root)
        while len(queue[-1]) != 0:
            queue.append([])
            for node in queue[-2]:
                if node.left != None:
                    queue[-1].append(node.left)
                if node.right != None:
                    queue[-1].append(node.right)
        result = []
        for i in range(len(queue)):
            if len(queue[i]) != 0:
                result.append([])
                for j in range(len(queue[i])):
                    result[i].append(queue[i][j].val)
        result = result[::-1]
        return result
        
        