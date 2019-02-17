'''Question:
Implement a method to perform basic string compression using the counts of 
repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. 

If the "compressed" string would not become smaller than the original string, 
your method should return the original string. 

You can assume the string has only uppercase and lowercase letters (a - z).
'''

import unittest
from test_utils import UnitTestBase

# time: O(n)
# space: O(n)
def str_comp(s):
  if s == '':
    return ''

  cur, ct, res = s[0], 0, ''
  for c in s:
    if c == cur:
      ct +=1
    else:
      # Note: res = res + cur + str(ct) will be very slow and result in not O(n)
      res += cur + str(ct)
      cur, ct = c, 1
  res += cur + str(ct)

  # another way to write it: min(s, res, key=len)
  return res if len(res) < len(s) else s

class TestStrComp(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      ('', ''), # 0
      ('a', 'a'), # 1
      ('aa', 'aa'), # 2
      ('aaa', 'a3'), # 3
      ('aaaa', 'a4'), # 4

      ('ab', 'ab'), # 11
      ('abb', 'abb'), # 12
      ('abbb', 'abbb'), # 13
      ('abbbb', 'a1b4'), #14
      ('aab', 'aab'), # 21
      ('aabb', 'aabb'), # 22
      ('aabbb', 'a2b3'), # 23
      ('aabbbb', 'a2b4'), # 24
      ('aaab', 'aaab'), # 31
      ('aaabb', 'a3b2'), # 32
      ('aaabbb', 'a3b3'), # 33
      ('aaabbbb', 'a3b4'), # 34
      ('aaaab', 'a4b1'), # 41
      ('aaaabb', 'a4b2'), # 42
      ('aaaabbb', 'a4b3'), # 43
      ('aaaabbbb', 'a4b4'), # 44

      ('abc', 'abc'), # 111
      ('abcc', 'abcc'), # 112
      ('abccc', 'abccc'), # 113
      ('abbc', 'abbc'), # 121
      ('abbcc', 'abbcc'), # 122
      ('abbccc', 'abbccc'), # 123
      ('abbbc', 'abbbc'), # 131
      ('abbbcc', 'abbbcc'), # 132
      ('abbbccc', 'a1b3c3'), # 133
      ('aabc', 'aabc'), # 211
      ('aabcc', 'aabcc'), # 212
      ('aabccc', 'aabccc'), # 213
      ('aabbc', 'aabbc'), # 221
      ('aabbcc', 'aabbcc'), # 222
      ('aabbccc', 'a2b2c3'), # 223
      ('aabbbc', 'aabbbc'), # 231
      ('aabbbcc', 'a2b3c2'), # 232
      ('aabbbccc', 'a2b3c3'), # 233
      ('aaabc', 'aaabc'), # 311
      ('aaabcc', 'aaabcc'), # 312
      ('aaabccc', 'a3b1c3'), # 313
      ('aaabbc', 'aaabbc'), # 321
      ('aaabbcc', 'a3b2c2'), # 322
      ('aaabbccc', 'a3b2c3'), # 323
      ('aaabbbc', 'a3b3c1'), # 331
      ('aaabbbcc', 'a3b3c2'), # 332
      ('aaabbbccc', 'a3b3c3'), # 333

      ('aabcccccaaa', 'a2b1c5a3'),
    ]

  def func_provider(self):
    return [
      str_comp,
    ]

  def func_eval(self, func, args):
    return func(args)

if __name__ == '__main__':
  unittest.main()