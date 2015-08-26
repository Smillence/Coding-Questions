'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # assume l1, l2 are not null
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode 
        :type l2: ListNode 
        :rtype: ListNode
        """
        l3 = ListNode(0)
        tail = l3
        while l1 or l2:
            if not tail.next:
                tail.next = ListNode(0)
            tail = tail.next
            if l1:
                tail.val += l1.val
                l1 = l1.next
            if l2:
                tail.val += l2.val
                l2 = l2.next
            if tail.val >= 10:
                tail.val -= 10
                tail.next = ListNode(1)
        return l3.next