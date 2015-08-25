'''
Write code to reverse a C-Style String. (C-String means that 'abcd' is represented as five characters, including the null character.)


In C and C++, strings are typically represented as char arrays that have a null terminator. A null terminator means that the string ends with a '\0' character (which has ASCII code 0)

'''


# clarification questions:
# 1) input is a string ending with '\0'
# 2) i cannot use .reverer(), right?
import copy
def strReverse(string):
    string = copy.deepcopy(string)
    string = string[:-1]
    lst = list(string)
    lst.reverse() # the same as: reverse(lst)  
    lst.append('\0')
    return str(lst)

# the same as list's reverse() function
def reverse(lst):
    # swap from the beginning to the middle point of the array
    for i in range(len(lst)/2):
        tmp = lst[i]
        right = len(lst) - 1 - i
        lst[i] = lst[right]
        lst[right] = tmp        
        
    return None

if __name__ == '__main__':
    print strReverse('abocd\0')
