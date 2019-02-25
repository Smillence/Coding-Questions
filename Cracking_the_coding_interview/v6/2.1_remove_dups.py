'''Question:
Write code to remove duplicates from an unsorted linked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

clarification:
- singly linked list? yes
- will there be circles? no
- can I assume the linked list only contains integer data? yes
- if thare are dups at position x and x+n, remove the one at x+n
- the order should be reserved
- what is a temporary buffer? it means even hash table cannot be used 
- return head
'''

import unittest
from test_utils import UnitTestBase
from data_structure import Node, LinkedList as LL

# Solution: use hash table
# Time: O(n)
# Space: O(n)
def remove_dups_1(ll):
  cur = ll.head
  if cur == None:
    return ll

  keys = set([cur.data])
  while cur.next != None:
    key = cur.next.data
    if key not in keys:
      keys.add(key)
      cur = cur.next
    else:
      cur.next = cur.next.next
    
  return ll

# Solution: no temporaty buffer
# Time: O(n*n)
# Space: O(1)
def remove_dups_2(ll):
  anchor = ll.head
  while anchor != None:
    cur, key = anchor, anchor.data

    while cur.next != None:
      if cur.next.data != key:
        cur = cur.next
      else:
        cur.next = cur.next.next

    anchor = anchor.next
    
  return ll

# Solution: no temporaty buffer. recursion
# Time: O(n*n)
# Space: O(1) - tail recursion
def remove_dups_3(ll):
  remove_dups_3_helper(ll.head)
  return ll

def remove_dups_3_helper(anchor):
    if anchor == None:
      return

    cur, key = anchor, anchor.data

    while cur.next != None:
      if cur.next.data != key:
        cur = cur.next
      else:
        cur.next = cur.next.next

    remove_dups_3_helper(anchor.next)

class Test(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      (LL(), LL()),
      (LL([1]), LL([1])),
      (LL([1, 2, 3]), LL([1, 2, 3])),
      (LL([1, 1]), LL([1])),
      (LL([4, 8, 2, 4]), LL([4, 8, 2])),
      (LL([4, 2, 2, 4]), LL([4, 2])),
      (LL([1, 4, 6, 8, 6, 2, 1]), LL([1, 4, 6, 8, 2])),
      (LL([4, 2, 3, 4, 8, 6, 6, 2]), LL([4, 2, 3, 8, 6])),
    ]

  def func_provider(self):
    return [
      remove_dups_1,
      remove_dups_2,
      remove_dups_3,
    ]

  def func_eval(self, func, args):
    return func(args)

if __name__ == '__main__':
  unittest.main()
