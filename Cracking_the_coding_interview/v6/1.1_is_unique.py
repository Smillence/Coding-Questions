'''Question:
implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures?
'''

'''
Confusions:
1. What do you mean by "all unique characters"? I assume it is ACSII string with
 value 0~255.
2. What do you mean by "cannot use addtional data structures"?
3. Does the string need to include all 256 characters? Or just need to have no
duplicates. (assume the later one)
Examples:
1) agshdhfkd -> False
2) agsdhfk -> True
'''
import unittest

# Solution: hash table
# time: O(n)
# space: O(1) - Note: there are only 256 characters
def is_unique_1(string):
    if len(string) > 256:
        return False

    s = set()
    for char in string:
        if char in s:
            return False
        else:
            s.add(char)
    return True

# Solution: similar to hash table
# time: O(n)
# space: O(1)
def is_unique_2(string):
    if len(string) > 256:
        return False

    char_set = [False for _ in range(256)]
    for char in string:
        # returns the integer ordinal of a character
        index = ord(char)
        if char_set[index]:
            return False
        else:
            char_set[index] = True
    return True

# Solution: bit vector
# Limitation: using int as bit vector will be very slow if there are millions of bits
# time: O(n)
# space: O(1)
def is_unique_3(string):
    if len(string) > 256:
        return False

    checker = 0
    for char in string:
        pos = ord(char)
        if (checker >> pos) & 1:
            return False
        else:
            checker |= 1 << pos
    return True

class TestIsUnique(unittest.TestCase):
    def data_provider(self):
        return [
            ('', True),
            ('a', True),
            ('~~', False),
            ('agshdhfkd', False),
            ('agsdhfk', True),
            ('agsdhfkA123BGW', True),
            ('agsdhfkA123BGW278', False),
            ('23ds2', False),
            ('hb 627jh=j ()', False),
        ];

    def func_provider(self):
        return [
            is_unique_1,
            is_unique_2,
            is_unique_3,
        ];

    def test(self):
        for func in self.func_provider():
            for input, expected in self.data_provider():
                output = func(input)
                self.assertEqual(
                    output,
                    expected,
                    "%s('%s') output: %r. Expect: %r" % (func.__name__, input, output, expected),
                )

if __name__ == '__main__':
    unittest.main()
