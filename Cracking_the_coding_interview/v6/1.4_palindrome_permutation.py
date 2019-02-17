'''Question:
Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same forwards and
backwards. A permutation is a rearrangement of letters. The palindrome does not
need to be limited to just dictionary words.

EXAMPLE
Input: tactcoa
Output: True
'''

import unittest
from collections import Counter

# Solution: hash table
# time: O(n)
# space: O(1) - there are only 256 possible characters
def palindrome_permutation_1(s):
    counter = Counter(s)
    has_odd_num_char = False
    for char, count in counter.items():
        if count % 2 != 0:
            if has_odd_num_char:
                return False
            has_odd_num_char = True
    return True

# Solution: same as 1. but use bit vector
def palindrome_permutation_2(s):
    checker = 0 # bit vector of length 256
    for c in s:
        checker ^= 1 << ord(c)

    # find out how many bits are set to 1
    has_odd_num_char = False
    while checker:
        if checker & 1:
            if has_odd_num_char:
                return False
            has_odd_num_char = True
        # Hot spot: it's wrong to write: checker >> 1. need to use >>=
        checker >>= 1
    return True

class TestPalindromePermutation(unittest.TestCase):
    def data_provider(self):
        return [
            ('', True),
            ('a', True),
            ('aab', True),
            ('aaaa', True),
            ('aaaba', True),
            ('abab', True),
            ('tactcoa', True),
            ('ab', False),
            ('aabc', False),
            ('jhsabckuj  ahjsbckj', True),
            ('able was I ere I saw elba', True),
            ('so patient a nurse to nurse a patient so', False),
            ('not a palindrome', False),
            ('no x in nixon', True),
        ]

    def func_provider(self):
        return [
            palindrome_permutation_1,
            palindrome_permutation_2,
        ]

    def test(self):
        for func in self.func_provider():
            for data in self.data_provider():
                s, expected = data
                err_msg = 'Failed ' + func.__name__ + '() case: ' + str(data)
                self.assertEqual(func(s), expected, err_msg)

if __name__ == '__main__':
    unittest.main()
