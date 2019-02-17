'''Question:
Given two strings, write a method to decide if one is a permutation of the
other.
'''
import unittest
from collections import defaultdict, Counter
from test_utils import UnitTestBase

# Solution: hash table
# time: O(n)
# space: O(1) - there are only 256 possible keys
def check_permutation_1(s1, s2):
  if len(s1) != len(s2):
    return False
  s1_char_count = defaultdict(int)
  for char in s1:
    s1_char_count[char] += 1
  for char in s2:
    if s1_char_count[char] == 0:
      return False
    s1_char_count[char] -= 1
  return True

# Solution: same as 1. but use Counter
def check_permutation_2(s1, s2):
  if len(s1) != len(s2):
    return False
  return Counter(s1) == Counter(s2)

class TestCheckPermutation(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      (('', ''), True),
      (('a', 'a'), True),
      (('ab', 'ba'), True),
      (('aab', 'aba'), True),
      (('aabc', 'baca'), True),
      (('abcd', 'bacd'), True),
      (('3563476', '7334566'), True),
      (('wef34f', 'wffe34'), True),
      (('a', ''), False),
      (('aa', 'a'), False),
      (('ab', 'ac'), False),
      (('aabc', 'bacb'), False),
      (('aabc', 'bacd'), False),
      (('abcd', 'd2cba'), False),
      (('2354', '1234'), False),
      (('dcw4f', 'dcw5f'), False),
    ]

  def func_provider(self):
    return [
      check_permutation_1,
      check_permutation_2,
    ]

  def func_eval(self, func, args):
    s1, s2 = args
    return func(s1, s2)

if __name__ == '__main__':
  unittest.main()
