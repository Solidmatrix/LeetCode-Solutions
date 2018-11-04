# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        hashmap = collections.defaultdict(int)
        for i, it in enumerate(inorder):
            hashmap[it] = i
        # hashmap = {}
        # for i in range(len(inorder)):
        #     hashmap[inorder[i]] = i
        
        def build(a, b, c, d):
            if a == b:
                return None
            if a+1 == b:
                return TreeNode(inorder[a])
            mid = postorder[d-1]
            m = hashmap[mid]
            root = TreeNode(mid)
            root.left = build(a, m, c, c+m-a)
            root.right = build(m+1, b, m-b+d, d-1)
            return root
       
        return build(0, len(inorder), 0, len(postorder))
