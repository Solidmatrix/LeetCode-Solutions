# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = l1
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + carry
            carry = sum / 10
            l1.val = sum % 10
            pre = l1
            l1 = l1.next
            l2 = l2.next
        if l2 != None:
            l1 = pre.next = l2
        while l1 != None:
            sum = l1.val + carry
            carry = sum / 10
            l1.val = sum % 10
            pre = l1
            l1 = l1.next
        if carry:
            pre.next = ListNode(1)
        return head
        