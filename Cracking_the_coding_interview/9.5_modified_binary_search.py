'''
9.5
Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.

Example: find 'ball' in ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', ''] will return 4

Example: find 'ballcar' in ['at', '', '', '', '', 'ball', 'car', '', '', 'dad', '', ''] will return -1
'''

# clarification quesitons:
# what do you mean by sorted array of string? (just use '<' to compare)
# increasing order? (yes)
# no duplicates? (no)
# the given string is no empty? (yes)
    
    
def indexOf(arr,s,pre):
    n = len(arr)
    if n==0:
        return -1
    if n==1:
        if arr[0] == s:
            return pre
        else:
            return -1
        
    # what is the size of arr
    # at least 2 here
    mid = n/2
    if arr[mid] != '':
        if s<arr[mid]:
            # what is the size of arr[:mid]?
            # at least 0
            return indexOf(arr[:mid],s,pre)
        else:
            # what is the size of arr[mid:]?
            # at least one
            return indexOf(arr[mid:],s,pre+mid)
    else:
        cur = None
        for i in range(mid,-1,-1):
            if arr[i] != '':
                cur = i
                break
        if cur != None:
            if s<=arr[cur]:
                return indexOf(arr[:cur+1],s,pre)
            else:
                return indexOf(arr[mid:],s,pre+mid)                
        else:
            return indexOf(arr[mid:],s,pre+mid)
        
        
        
        
    
    
if __name__ == '__main__': 
    arr =  ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
    print indexOf(arr,'ball',0)
    print indexOf(arr,'ballc',0)
    print indexOf(arr,'car',0)
    print indexOf(arr,'dad',0)
    print indexOf(arr,'at',0)
    
    
