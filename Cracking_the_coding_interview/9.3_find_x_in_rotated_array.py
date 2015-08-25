'''
9.3
Given a sorted array of n integers that has been rotated an unknown number of times, give an O(log n) algorithm that finds an element in the array. You may assume that the array was originally sorted in increasing order.
EXAMPLE:
Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
Output: 8 (the index of 5 in the array)
'''

# clarification quesitons:
# 1) no duplicates in the array? (no)
# 2) what if the given number not in the array? (return None)
# 3) rotated unknown times is same as rotated once? (yes)


    
    
def indexOf(x,arr,pre):
    n = len(arr)
    
    if n == 1:
        if arr[0] == x: 
            return pre
        else:
            return None
    
    head = arr[0]
    mid = arr[n/2]
    
    if head<mid:
        if head<=x<mid:
            return indexOf(x,arr[:n/2],pre)
        else:
            return indexOf(x,arr[n/2:],pre+n/2)
    else:
        if mid<=x<head:
            return indexOf(x,arr[n/2:],pre+n/2)
        else:
            return indexOf(x,arr[:n/2],pre)    
    
if __name__ == '__main__': 
    arr = [15,16,19,20,25,1,3,4,5,7,10,14]
    print indexOf(5,arr,0)
    