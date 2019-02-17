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
2. return true if one or zero edits away, else false

Solution:
1. replace case is easy. if same length, compare characters one by one
2. insert case and remove case is the same technically.
'''

import unittest

# time: O(n)
# space: O(1)
def one_away_1(s1, s2):
    if len(s1) == len(s2):
        num_mistach = 0
        for i in range(len(s1)): # there is another way to write this: for c1, c2 in zip(s1, s2):
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
        # Hot spot 1: it's also important to check s_shorter lenght. The reason is
        # if s_shorter is empty string, line 39 will have out-of-index error
        while i < len(s_longer) and j < len(s_shorter):
            if s_longer[i] != s_shorter[j]:
                if num_mistach >= 1:
                    return False
                num_mistach += 1
                i += 1
            # Hot spot 2: it's easy to assume no matter what, we will do i++ j++
            # at the end of the loop. But this is wrong because 'pabe', 'ple'
            # will fail. The trick is if a != l, we need to move index i but not
            # j. we still need to check if b != l
            else:
                i += 1
                j += 1
        return True
    return False

# time: O(n)
# space: O(1)
def one_away_2(s1, s2):
    if len(s1) <= len(s2):
        return one_away_2_helper(s1, s2)
    else:
        return one_away_2_helper(s2, s1)

# pre-requisite: len(s1) <= len(s2)
def one_away_2_helper(s1, s2):
    dist = len(s2) - len(s1)
    if dist > 1:
        return False

    if dist == 0:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[i+1:] == s2[i+1:] # it's ok if reaches end of string
        return True

    # dist is 1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return s1[i:] == s2[i+1:]
    return True

# time: O(n)
# space: O(1)
def one_away_3(s1, s2):
    if len(s1) <= len(s2):
        return one_away_3_helper(s1, s2)
    else:
        return one_away_3_helper(s2, s1)

''' 
pre-requisite: len(s1) <= len(s2)
Note: this solution is more elegant comparing to one_away_2_helper because it
does not need to compare dist with 0 or 1 before the for-loop. It does all three
checks in a single pass.
''' 
def one_away_3_helper(s1, s2):
    dist = len(s2) - len(s1)

    if dist > 1: # Hot spot 3: w/o this special case, it will fail test case ('', 'ab')
        return False

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue

        pos = i+1 if dist == 0 else i
        return s1[pos:] == s2[i+1:]
 
    # Hot spot 4: case ('pal', 'palks') can be missed easily
    return True

class TestOneAway(unittest.TestCase):
    def data_provider(self):
        return [
            ('', '', True),
            ('a', 'a', True),
            ('a', '', True),
            ('', 'a', True),
            ('a', 'b', True),
            ('a', 'ab', True),
            ('ab', 'ba', False),
            ('ab', '', False),
            ('pale', 'pale', True),
            ('pale', 'ple', True),
            ('ple', 'pale', True),
            ('pale', 'ble', False),
            ('pale', 'pas', False),
            ('pas', 'pale', False),
            ('pabe', 'ple', False),
            ('pale', 'pse', False),
            ('pales', 'pale', True),
            ('ples', 'pales', True),
            ('pale', 'bale', True),
            ('pale', 'pkle', True),
            ('pkle', 'pable', False),
            ('pal', 'palks', False),
            ('palks', 'pal', False),
            ('pale', 'bake', False),
            ('paleabc', 'pleabc', True),
        ]

    def func_provider(self):
        return [
            one_away_1,
            one_away_2,
            one_away_3,
        ]

    def test(self):
        for func in self.func_provider():
            for data in self.data_provider():
                s1, s2, expected = data
                err_msg = 'Failed ' + func.__name__ + '() case: ' + str(data)
                self.assertEqual(func(s1, s2), expected, err_msg)

if __name__ == '__main__':
    unittest.main()
