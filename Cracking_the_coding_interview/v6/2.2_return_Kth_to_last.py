'''Question:
Implement an algorithm to find the kth to last element of a singly linked list

clarification:
- what is the Kth to last element? if K is 1, should I return the last element? yes
- should K be positive integers? yes
- what if K is outside of index? return None
- what to return for empty list? None
- can there be cycles? no
- should I return the node object or the value in it? the value in it
'''

import unittest
from test_utils import UnitTestBase
from data_structure import LinkedList as LL

# Solution: keep two pointers
# Time: O(n)
# Space: O(1)
def return_kth_to_last(ll, k):
  chaser = ll.head
  runner = ll.head
  for _ in range(k):
    if runner == None:
      return None
    runner = runner.next

  while runner != None:
    chaser = chaser.next
    runner = runner.next

  return chaser.data

class Test(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      ((LL(), 1), None),
      ((LL([1]), 1), 1),
      ((LL([1]), 2), None),
      ((LL([1, 2]), 1), 2),
      ((LL([1, 2]), 2), 1),
      ((LL([1, 2]), 3), None),
      ((LL([1, 2, 3]), 1), 3),
      ((LL([1, 2, 3]), 2), 2),
      ((LL([1, 2, 3]), 3), 1),
      ((LL([1, 2, 3]), 4), None),
      ((LL([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 3), 7),
    ]

  def func_provider(self):
    return [
      return_kth_to_last,
    ]

  def func_eval(self, func, args):
    ll, k = args
    return func(ll, k)

if __name__ == '__main__':
  unittest.main()
