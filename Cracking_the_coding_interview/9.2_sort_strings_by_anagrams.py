'''
9.2
Write a method to sort an array of strings so that all the anagrams are next to each other.
'''

# clarification quesitons:
# no order for anagrams (yes)



# the idea is to do a modified version of traditional string comparison
# use merge sort


    
    
def mergesort(Input,function):
    if len(Input) <= 1: return Input
    
    mid = len(Input)/2
    left = mergesort(Input[:mid],function)
    right = mergesort(Input[mid:],function)
    return merge(left,right,function) 
 
def merge(L,R,function):
    if not L:
        return R
    if not R:
        return L   
    
    if function(L[0],R[0]):
        if type(L) == type([]):
            return [L[0]] + merge(L[1:],R,function)
        if type(L) == type(''):
            return L[0] + merge(L[1:],R,function)
    else:
        if type(L) == type([]):
            return [R[0]] + merge(L,R[1:],function) 
        if type(L) == type(''):
            return R[0] + merge(L,R[1:],function) 
       
def charCompare(a,b):
    return a <= b

def stringCompare(s1,s2):
    s1 = mergesort(s1,charCompare)
    s2 = mergesort(s2,charCompare)
    return s1<=s2
    
    
if __name__ == '__main__':  
    print mergesort('bac',charCompare)
    arr = ['abc','ac','acb','ca','cba']    
    print mergesort(arr,stringCompare)