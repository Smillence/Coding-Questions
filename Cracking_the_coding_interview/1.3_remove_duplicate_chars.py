'''
Design an algorithm and write code to remove the duplicate characters in a 
string without using any additional buffer. NOTE: One or two additional 
variables are fine. An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.
'''

# clarification question:
# 1) does order matter? If not simple use ''.join(set(string) will work (yes, 
#    it matters)
# 2) for duplicates, we keep its first occurance. is that correct? (yes)
# 3) what do you mean by 'An extra copy of the array'?
#    i plan to use a dictionary to store unique chars, is this allowed?
#    (yes)
# 4) can I use python's set? (yes)
# 5) can I use python's collections library? (yes)

# solution 1: use Set
# order matters
def remove_duplicates_1(string):
    uniques = list(set(string))
    lst = list(string)
    for i in range(len(lst)):
        char = lst[i]
        if char in uniques:
            uniques.remove(char)
        else:
            lst[i] = ''
    return ''.join(lst)
    
# solution 2: use OrderedDict
# order matters
from collections import OrderedDict
def remove_duplicates_2(string):
    return ''.join(OrderedDict.fromkeys(string))
 
    
# solution 3: scan from the beginning, remove all duplicates
# order matters
# time: O(n^2)
# space: O(1)
def remove_duplicates_3(string):
    lst = list(string)
    for i in range(len(lst)-1):
        char = lst[i]
        for j in range(i+1,len(lst)):
            if lst[j] == char:
                lst[j] = ''
    return ''.join(lst)

# solution 4: use Set
# order does not matter
def remove_duplicates_4(string):  
    return ''.join(set(string))


# solution 5: do use use Set
# order does not matter
def remove_duplicates_5(string):  
    lst = list(string)
    lst.sort()#O(nlogn)
    cur = None
    for i in range(len(lst)):
        if lst[i] != cur:
            cur = lst[i]
        else:
            lst[i] = ''
    return ''.join(lst)

# solution 6: use hash table
# order does matter
# input is a char list
# assume it is ACSII string with value 0~255
def hash_function(char):
    return ord(char)
def remove_duplicates_6(lst):
    table = [False for x in range(256)]
    length = len(lst)
    cur = 0
    while cur < length:
        char = lst[cur]
        index = hash_function(char)
        if table[index] == False:
            table[index] = True
            cur += 1
        else:
            del lst[cur]
            length -= 1        
    return lst
 
''' Below are unit tests ''' 

def test_order_matters(sol):
    success = sol('abdcda') == 'abdc'
    success = success and sol('ab') == 'ab'
    success = success and sol('aa') == 'a'
    success = success and sol('a') == 'a'
    success = success and sol('') == ''
    name = sol.__name__
    if success:
        print "%s passed all test cases!" % name
    else:
        print "Sorry, %s failed the test cases." % name

def test_order_does_not_matters(sol):
    success = set(sol('abdcda')) == set('abdc')
    success = success and set(sol('ab')) == set('ab')
    success = success and set(sol('aa')) == set('a')
    success = success and set(sol('a')) == set('a')
    success = success and set(sol('')) == set('')
    name = sol.__name__
    if success:
        print "%s passed all test cases!" % name
    else:
        print "Sorry, %s failed the test cases." % name

def test_sol_6(sol):
    success = ''.join(sol(list('abdcda'))) == 'abdc'
    success = success and ''.join(sol(list('ab'))) == 'ab'
    success = success and ''.join(sol(list('aa'))) == 'a'
    success = success and ''.join(sol(list('a'))) == 'a'
    success = success and ''.join(sol(list(''))) == ''
    name = sol.__name__
    if success:
        print "%s passed all test cases!" % name
    else:
        print "Sorry, %s failed the test cases." % name
      
if __name__ == '__main__':
    test_order_matters(remove_duplicates_1)
    test_order_matters(remove_duplicates_2)
    test_order_matters(remove_duplicates_3)
    test_order_does_not_matters(remove_duplicates_4)
    test_order_does_not_matters(remove_duplicates_5)
    test_sol_6(remove_duplicates_6)
