'''Question:
Given two strings, write a method to decide if one is a permutation of the
other.
'''
import unittest
from collections import defaultdict

# Solution: hash table
# time: O(n)
# space: O(1) - there are only 256 possible keys
def check_permutation(s1, s2):
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

class TestCheckPermutation(unittest.TestCase):
    def data_provider(self):
        return [
            ('', '', True),
            ('a', 'a', True),
            ('ab', 'ba', True),
            ('aab', 'aba', True),
            ('aabc', 'baca', True),
            ('a', '', False),
            ('aa', 'a', False),
            ('ab', 'ac', False),
            ('aabc', 'bacb', False),
            ('aabc', 'bacd', False),
        ]

    def test(self):
        for s1, s2, expected in self.data_provider():
            output = check_permutation(s1, s2)
            self.assertEqual(
                output,
                expected,
                "check_permutation('%s', '%s') output: %r. Expect: %r" % (s1, s2, output, expected),
            )

if __name__ == '__main__':
    unittest.main()
