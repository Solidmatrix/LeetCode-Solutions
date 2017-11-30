# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        index = {}
        p = head
        q = new = RandomListNode(0)
        while p != None:
            q.next = RandomListNode(p.label)
            index[p] = q = q.next
            p = p.next
        p = head
        while p != None:
            if p.random != None:
                index[p].random = index[p.random]
            p = p.next
        return new.next
            
            
            
            
            