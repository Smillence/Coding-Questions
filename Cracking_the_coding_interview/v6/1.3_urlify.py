'''Question:
Write a method to replace all spaces in a string with '%20'. You may assume that
the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string. (Note: If implementing
in Java, please use a character array so that you can perform this operation in
place.)
EXAMPLE
Input:  "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"
Hints: #53, #118

Clarifications:
1. "You may assume that the string has sufficient space" does this mean the
actual space might be larger than necessary? yes
2. what is the "true" lenght of a string? in python, it should be len(s)
3. when computing the "true" lenght of a string, tailing spaces will be counted
as well. yes
4. input will be a char array with an int and output will be the same char array? yes
5. so the input char array will be altered? yes
6. so there might be some garbage in the end of the array? yes
'''
import unittest

REPLACER = '%20'

# Solution: find # of spaces before n; edit string from n-1
# time: O(n)
# space: O(1)
def urlify(char_array, n):
    num_of_spaces = 0
    for i in range(n):
        if is_space(char_array[i]):
            num_of_spaces += 1

    cursor = num_of_spaces * (len(REPLACER) - 1) + (n - 1)
    for i in range(n - 1, -1, -1):
        if is_space(char_array[i]):
            char_array[cursor - len(REPLACER) + 1 : cursor + 1] = list(REPLACER)
            cursor -= len(REPLACER)
        else:
            char_array[cursor] = char_array[i]
            cursor -= 1
    return char_array

def is_space(c):
    return c == ' '

def char_array_2_str(char_array):
    return ''.join(char_array)

class TestCheckPermutation(unittest.TestCase):
    def data_provider(self):
        return [
            ('Mr John Smith$#%^', 13, 'Mr%20John%20Smith'),
            ('Mr John Smith $#%^&*', 14, 'Mr%20John%20Smith%20'),
            ('', 0, ''),
            ('a', 0, 'a'),
            ('a', 1, 'a'),
            (' %^', 1, '%20'),
            ('Ha$#%^&*', 2, 'Ha$#%^&*'),
            ('Ha ha$#%^&*', 5, 'Ha%20ha%^&*'),
        ]

    def func_provider(self):
        return [
            urlify,
        ]

    def test(self):
        for func in self.func_provider():
            for data in self.data_provider():
                s, n, expected = data
                self.assertEqual(len(s), len(expected), func.__name__ + '() case: ' + str(data) + ' corrupted')

                err_msg = func.__name__ + '() case: ' + str(data) + ' failed'

                char_array = list(s)
                output = func(char_array, n)
                self.assertEqual(char_array, output, err_msg)

                output_2_str = char_array_2_str(output)
                self.assertEqual(output_2_str, expected, err_msg)

if __name__ == '__main__':
    unittest.main()
