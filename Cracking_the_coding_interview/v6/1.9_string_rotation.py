'''Question:
Assume you have a method `isSubstring` which checks if one word is a substring 
of another. Given two strings, s1 and s2, write code to check if s2 is a 
rotation of s1 using only one call to isSubstring (e.g.,"waterbottle" is a 
rotation of"erbottlewat").

clarification:
- define rotation: X is a rotation of Y if X can be represented as M|N where Y
can be represented as N|M 
- is the string it self its rotation? Yes
'''

import unittest
from test_utils import UnitTestBase

'''
Common solution would be checking char by char from the beginning. But that
will result in O(N*N)

Hint: do I need to find out the exact position where the rotation happened?
'''
def is_rotation(s1, s2):
  if len(s1) != len(s2):
    return False

  return is_substring(s1 * 2, s2)

def is_substring(s1, s2):
  return s2 in s1

class Test(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      (('', ''), True),
      (('a', 'a'), True),
      (('a', 'b'), False),
      (('a', 'ab'), False),
      (('ab', 'ab'), True),
      (('ab', 'ba'), True),
      (('ab', 'ac'), False),
      (('ab', 'cd'), False),
      (('abc', 'abc'), True),
      (('abc', 'bca'), True),
      (('abc', 'cab'), True),
      (('abcd', 'abcd'), True),
      (('abcd', 'bcda'), True),
      (('abcd', 'cdab'), True),
      (('abcd', 'dabc'), True),
      (('abcd', 'bcad'), False),
      (('waterbottle', 'erbottlewat'), True),
    ]

  def func_provider(self):
    return [
      is_rotation,
    ]

  def func_eval(self, func, args):
    s1, s2 = args
    return func(s1, s2)

if __name__ == '__main__':
  unittest.main()