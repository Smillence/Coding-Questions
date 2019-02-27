'''Question:
You have two numbers represented by a linked list, where each node contains a 
single digit.The digits are stored in reverse order, such that the 1 's digit 
is at the head of the list. Write a function that adds the two numbers and 
returns the sum as a linked list.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.

Clarification:
- will there be any circles? no
- can I assume both linked lists won't be empty? yes
'''

import unittest
from test_utils import UnitTestBase
from data_structure import Node, LinkedList as LL

# Time: O(Max(M, N))
# Space: O(Max(M, N))
def sum_lists_1(ll1, ll2):
  cur = head = Node(None) # dummy node
  carry, pt1, pt2 = 0, ll1.head, ll2.head
  while pt1 != None or pt2 != None or carry != 0:
    tmp = carry
    if pt1 != None:
      tmp += pt1.data
      pt1 = pt1.next
    if pt2 != None:
      tmp += pt2.data
      pt2 = pt2.next
    carry, value = tmp // 10, tmp % 10
    cur.next = Node(value)
    cur = cur.next

  return LL(head.next)

# Solution: use recursion
# Time: O(Max(M, N))
# Space: O(Max(M, N))
def sum_lists_2(ll1, ll2):
  head = sum_lists_2_helper(ll1.head, ll2.head, 0)
  ll = LL([])
  ll.head = head
  return ll

def sum_lists_2_helper(node1, node2, carry):
  if node1 == None and node2 == None and carry == 0:
    return None

  tmp = carry
  if node1 != None:
    tmp += node1.data
  if node2 != None:
    tmp += node2.data

  new_carry, value = tmp // 10, tmp % 10

  next = sum_lists_2_helper(
    node1.next if node1 != None else None,
    node2.next if node2 != None else None,
    new_carry,
  )
  return Node(value, next)

# assume ll1 and ll2 has at least 1 node
def sum_lists_follow_up(ll1, ll2):
  len1, len2 = ll1.length(), ll2.length()
  head1, head2 = ll1.head, ll2.head
  if len1 < len2:
    head1 = append_zero_nodes(head1, len2 - len1)
  elif len1 > len2:
    head2 = append_zero_nodes(head2, len1 - len2)
  head = sum_lists_follow_up_helper(head1, head2)
  ll = LL([])
  ll.head = head
  return ll

# input: n must be positive integer
def append_zero_nodes(node, num):
  pt = head = Node(0)
  for _ in range(num - 1):
    pt.next = Node(0)
    pt = pt.next
  pt.next = node
  return head

def sum_lists_follow_up_helper(node1, node2):
  pass

class Test(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      ((LL([1]), LL([1])), LL([2])),
      ((LL([1]), LL([9])), LL([0, 1])),
      ((LL([7, 1, 6]), LL([5, 9, 2])), LL([2, 1, 9])),
      ((LL([1]), LL([9, 9, 9])), LL([0, 0, 0, 1])),
      ((LL([9, 7, 8]), LL([6, 8, 5])), LL([5, 6, 4, 1])),
    ]

  def func_provider(self):
    return [
      sum_lists_1,
      sum_lists_2,
    ]

  def func_eval(self, func, args):
    ll1, ll2 = args
    return func(ll1, ll2)

# class TestFollowUp(UnitTestBase, unittest.TestCase):
#   def data_provider(self):
#     return [
#       ((LL([1]), LL([1])), LL([2])),
#       ((LL([1]), LL([9])), LL([1, 0])),
#       ((LL([6, 1, 7]), LL([2, 9, 5])), LL([9, 1, 2])),
#       ((LL([1]), LL([9, 9, 9])), LL([1, 0, 0, 0])),
#     ]

#   def func_provider(self):
#     return [
#       sum_lists_follow_up,
#     ]

#   def func_eval(self, func, args):
#     ll1, ll2 = args
#     return func(ll1, ll2)

if __name__ == '__main__':
  unittest.main()
