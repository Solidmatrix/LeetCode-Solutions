# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == q:
            return p
        path = []
        path.append(root)
        while True:         #find the path of p or q, begin from root
            tmp = path[len(path)-1]
            if tmp == p or tmp == q:
                unknown = p if tmp == q else q
                break
            if tmp.left != None:
                path.append(tmp.left)
            elif tmp.right != None:
                path.append(tmp.right)
            else:
                prev = path[len(path)-2]
                while prev.right == tmp or prev.right == None:
                    path.pop()
                    tmp = prev
                    prev = path[len(path)-2]
                path.pop()
                path.append(prev.right)
        path1 = [] + path
        while True:         #find the path of the rest node, begin from the place we stopped
            tmp = path[len(path)-1]
            if tmp == unknown:
                break
            if tmp.left != None:
                path.append(tmp.left)
            elif tmp.right != None:
                path.append(tmp.right)
            else:
                prev = path[len(path)-2]
                while prev.right == tmp or prev.right == None:
                    path.pop()
                    tmp = prev
                    prev = path[len(path)-2]
                path.pop()
                path.append(prev.right)
        path2 = path
        length = min(len(path1), len(path2))      #compare the two paths
        for i in xrange(length):
            if path1[i] != path2[i]:
                return path1[i-1]
        return path1[length-1]
            
            
        
                
                