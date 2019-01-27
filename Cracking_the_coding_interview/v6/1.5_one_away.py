'''Question:
There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, write
a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false

Clarifications:
1. can I make my solution to be generic to X edit away?
let's focus on the initial question for now
'''

import unittest

# time: O(n)
# space: O(1)
def one_away_1(s1, s2):
    if len(s1) == len(s2):
        num_mistach = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if num_mistach >= 1:
                    return False
                num_mistach += 1
        return True
    elif abs(len(s1) - len(s2)) == 1:
        if len(s1) > len(s2):
            s_longer, s_shorter = s1, s2
        else:
            s_longer, s_shorter = s2, s1
        i, j, num_mistach = 0, 0, 0
        # Hot spot: it's also important to check s_shorter lenght. The reason is
        # if s_shorter is empty string, line 39 will have out-of-index error
        while i < len(s_longer) and j < len(s_shorter):
            if s_longer[i] != s_shorter[j]:
                if num_mistach >= 1:
                    return False
                num_mistach += 1
                i += 1
            # Hot spot: it's easy to assume no matter what, we will do i++ j++
            # at the end of the loop. But this is wrong because 'pabe', 'ple'
            # will fail. The trick is if a != l, we need to move index i but not
            # j. we still need to check if b != l
            else:
                i += 1
                j += 1
        return True
    return False

def one_away_2(s1, s2):
    pass

class TestOneAway(unittest.TestCase):
    def data_provider(self):
        return [
            ('', '', True),
            ('a', 'a', True),
            ('a', '', True),
            ('a', 'b', True),
            ('ab', 'ba', False),
            ('ab', '', False),
            ('pale', 'ple', True),
            ('pabe', 'ple', False),
            ('pales', 'pale', True),
            ('pale', 'bale', True),
            ('pale', 'bake', False),
        ]

    def func_provider(self):
        return [
            one_away_1,
        ]

    def test(self):
        for func in self.func_provider():
            for data in self.data_provider():
                s1, s2, expected = data
                err_msg = 'Failed ' + func.__name__ + '() case: ' + str(data)
                self.assertEqual(func(s1, s2), expected, err_msg)

if __name__ == '__main__':
    unittest.main()
