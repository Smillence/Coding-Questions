'''Question:
 Implement an algorithm to delete a node in the middle (i.e., any node but the 
 first and last node, not necessarily the exact middle) of a singly linked list,
 given only access to that node.

EXAMPLE
Input: the node c from the linked list a->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f

'''

import copy
import unittest
from test_utils import UnitTestBase
from data_structure import LinkedList as LL

# Time: O(1)
# Space: O(1)
def delete_middle_node(node):
  node.data = node.next.data
  node.next = node.next.next

class Test(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      ((LL([1, 2, 3]), 1), LL([1, 3])),
      ((LL([0, 1, 2, 3, 4, 5]), 2), LL([0, 1, 3, 4, 5])),
    ]

  def func_provider(self):
    return [
      delete_middle_node,
    ]

  def single_test(self, func, data):
    cpy = copy.deepcopy(data)
    ll, index = data[0]
    func(ll.get(index))
    self.expect(ll, func, cpy)

if __name__ == '__main__':
  unittest.main()
