'''Question:
implement an algorithm to determine if a string has all unique characters. 
What if you can not use additional data structures?
'''

'''Algorithm Design
Confusions:
1. What do you mean by "all unique characters"? I assume it is ACSII string with
 value 0~255.
2. What do you mean by "cannot use addtional data structures"? I assume I can 
only use string.
Examples:
1) agshdhfkd -> False
2) agsdhfk -> True
Design:
	Create a hash function to map all unique characters
'''

def hash_function(char):
    return ord(char)
    
# time: O(n)
# space: O(1) - fixed size 256
def all_unique_string(string):
    table = [0 for x in range(256)]
    for char in string:
        index = hash_function(char)
        if table[index] == 0:
            table[index] = 1
        else:
            return False
    return True

if __name__ == '__main__':
    print all_unique_string('agshdhfkd')
    print all_unique_string('agsdhfk')




