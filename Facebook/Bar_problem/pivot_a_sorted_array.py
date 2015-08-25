'''
You are given an integer K, and a sorted array as an input which has been rotated about an unknown pivot. For example, 4 5 6 7 8 9 1 2 3. 
We need to write a function which should return the index of K in the array, if K is present, else return -1.

'''

# clafirication questions:
# 1) for sorted, do you mean it is in increasing order or either can do?
# 2) can duplicate exists?
# 3) minimum length? say [1,2], it has two possible orderings


#[3,3,4,5,6,7,8,8,9,1,2,3,3]
# pivot: 9 - index 8

# Assume: increasing order; no duplicates; at least 3 elements;
def foo(K,lst):
    # edge case 1
    if K not in lst:
        return -1
    
    size = len(lst) # 9
    
    # edge case 2
    if size == 1: 
        return 0
    
    
    pivot = None
    increasing = False
    for i in range(1,size):
        if lst[i] < lst[i-1]:
            pivot = i
            break
            
    
    # pivot: 6
    # for current i < pivot: previous index is i+size-pivot; else: previous index is i-pivot
    # for previous i < pivot: index -> index + size - pivot; else: index --> index  - pivot
    # 0 -> 6; 1 -> 7; 2 -> 8; 3 -> 0; ...; 8 -> 5
    
    curIndex = lst.index(K) # 7
    if curIndex < pivot:
        return curIndex + size - pivot
    else:
        return curIndex - pivot
    
    
if __name__ == '__main__':
    lst = [4,5,6,7,8,9,1,2,3]
    print foo(4,lst)