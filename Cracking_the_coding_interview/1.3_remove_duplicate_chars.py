'''
Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer. NOTE: One or two additional variables are fine. An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.
'''

# clarification question:
# 1) does order matter? If not simple use ''.join(set(string) will work (yes, it matters)
# 2) for duplicates, we keep its first occurance. is that correct? (yes)
# 3) what do you mean by 'An extra copy of the array'?
#    i plan to use a dictionary to store unique chars, is this allowed?
#    (yes)
# 4) can I use python's set? (yes)
# 5) can I use python's collections library? (yes)

# solution 1: use Set
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
from collections import OrderedDict
def remove_duplicates_2(string):
    return ''.join(OrderedDict.fromkeys(string))
 
    
# solution 3: scan from the beginning, remove all duplicates of index - O(n^2)
def remove_duplicates_3(string):
    lst = list(string)
    for i in range(len(lst)-1):
        char = lst[i]
        for j in range(i+1,len(lst)):
            if lst[j] == char:
                lst[j] = ''
    return ''.join(lst)

# solution 4: if order does not matter, use Set
def remove_duplicates_4(string):  
    return ''.join(set(string))


# solution 5: if order does not matter (cannot use Set):
# 1) merge sort O(nlogn)
# 2) remove duplicates O(n)
def remove_duplicates_5(string):  
    lst = list(string)
    lst.sort()
    cur = None
    for i in range(len(lst)):
        if lst[i] != cur:
            cur = lst[i]
        else:
            lst[i] = ''
    return ''.join(lst)
    
      
if __name__ == '__main__':
    print remove_duplicates_5('abdcda')
    print remove_duplicates_5('ab')
    print remove_duplicates_5('aa')
    print remove_duplicates_5('a') 
    print remove_duplicates_5('')
    
    
    