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


# Solution: hash table
# time: O(n)
# space: O(1) - Note: there are only 256 characters
def is_unique_1(string):
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
    table = [0 for x in range(256)]
    for char in string:
        # returns the integer ordinal of a character
        index = ord(char)
        if table[index] == 0:
            table[index] = 1
        else:
            return False
    return True

# Solution: bit vector
# Limitation: using int as bit vector will be very slow if there are millions of bits
# time: O(n)
# space: O(1)
def is_unique_3(string):
    checker = 0
    for char in string:
        pos = ord(char)
        if (checker >> pos) & 1:
            return False
        else:
            checker |= 1 << pos
    return True

''' Below are Unit Tests '''

def unit_test_1(func):
    input_string = 'agshdhfkd'
    expected = False
    if func(input_string) == expected:
        print "Pass: Unit Test 1"
    else:
        print "Fail: Unit Test 1"

def unit_test_2(func):
    input_string = 'agsdhfk'
    expected = True
    if func(input_string) == expected:
        print "Pass: Unit Test 2"
    else:
        print "Fail: Unit Test 2"

def unit_test_3(func):
    input_string = 'agsdhfkA123BGW'
    expected = True
    if func(input_string) == expected:
        print "Pass: Unit Test 3"
    else:
        print "Fail: Unit Test 3"

def unit_test_4(func):
    input_string = 'agsdhfkA123BGW278'
    expected = False
    if func(input_string) == expected:
        print "Pass: Unit Test 4"
    else:
        print "Fail: Unit Test 4"

def run_unit_tests(func):
    unit_test_1(func)
    unit_test_2(func)
    unit_test_3(func)
    unit_test_4(func)

if __name__ == '__main__':
    run_unit_tests(is_unique_1)
    run_unit_tests(is_unique_2)
    run_unit_tests(is_unique_3)
