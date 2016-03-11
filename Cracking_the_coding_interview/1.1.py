'''Question:
implement an algorithm to determine if a string has all unique characters. 
What if you can not use additional data structures?
'''

'''
Confusions:
1. What do you mean by "all unique characters"? I assume it is ACSII string with
 value 0~255.
2. What do you mean by "cannot use addtional data structures"? I assume I can 
only use string.
3. Does the string need to include all 256 characters? Or just need to have no 
duplicates. (assume the later one)
Examples:
1) agshdhfkd -> False
2) agsdhfk -> True
'''

# Idea: hash table
# time: O(n)
# space: O(1) - fixed size 256
def all_unique_character_1(string):
    table = [0 for x in range(256)]
    for char in string:
        # ord returns the integer ordinal of a one-character string
        index = ord(char)
        if table[index] == 0:
            table[index] = 1
        else:
            return False
    return True

# Idea: hash table
# time: ?
# space: O(1)
def all_unique_character_2(string):
    table = []
    for char in string:
        if char in table:
            return False
        table.append(char)
    return True

# Idea: use bit vector, since Mac OS is in 64 bit, we need 4 vectors
# time: O(n)
# space: O(1)
def all_unique_character_3(string):
    checker_1 = checker_2 = checker_3 = checker_4 = 0
    for char in string:
        order = ord(char)
        if order < 64:
            if (checker_1 & (1<<order)) != 0:
                return False
            checker_1 |= 1<<order
        elif order < 128:
            order -= 64
            if (checker_2 & (1<<order)) != 0:
                return False
            checker_2 |= 1<<order
        elif order < 192:
            order -= 128
            if (checker_3 & (1<<order)) != 0:
                return False
            checker_3 |= 1<<order
        else:
            order -= 192
            if (checker_4 & (1<<order)) != 0:
                return False
            checker_4 |= 1<<order
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
    run_unit_tests(all_unique_character_1)
    run_unit_tests(all_unique_character_2)
    run_unit_tests(all_unique_character_3)
