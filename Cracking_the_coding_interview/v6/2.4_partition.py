'''Question:
Write code to partition a linked list around a value x, such that all nodes 
less than x come before all nodes greater than or equal to x. If x is contained 
within the list, the values of x only need to be after the elements less than x 
(see below). The partition element x can appear anywhere in the "right 
partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1[partition=5] 
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

Clarification:
- will the original linked list be modified? yes
- do I need to keep order? no
'''

import unittest
from test_utils import UnitTestBase
from data_structure import LinkedList as LL

# Time: O(n)
# Space: O(1)
def partition(ll, x):
  cur = ll.head
  if cur == None:
    return ll
  while cur.next != None:
    if cur.next.data >= x:
      cur = cur.next
    else:
      node = cur.next
      cur.next = node.next
      node.next = ll.head
      ll.head = node
  return ll

class Test(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      ((LL(), 1), LL()),
      ((LL([1, 2, 3]), 2), LL([1, 2, 3])),
      ((LL([1, 3]), 2), LL([1, 3])),
      ((LL([3, 1]), 2), LL([1, 3])),
      ((LL([1, 2, 3, 4, 5]), 4), LL([3, 2, 1, 4, 5])),
      ((LL([1, 2, 3, 5]), 4), LL([3, 2, 1, 5])),
      ((LL([3, 2, 1]), 2), LL([1, 3, 2])),
      ((LL([3, 5, 8, 5, 10, 2, 1]), 5), LL([1, 2, 3, 5, 8, 5, 10])),
    ]

  def func_provider(self):
    return [
      partition,
    ]

  def func_eval(self, func, args):
    ll, x = args
    return func(ll, x)

if __name__ == '__main__':
  unittest.main()
