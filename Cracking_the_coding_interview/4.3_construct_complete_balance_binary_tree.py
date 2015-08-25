'''
4.3
Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.
'''

'''
Algorithm:
1. Insert into the tree the middle element of the array
2. Insert (into the left subtree) the left subarray elements
3. Insert (into the right subtree) the right subarray elements 4. Recurse
'''

class Tree:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val
    def __str__(self,level=0):
        ret = "\t"*level+repr(self.data)+"\n"
        if self.right:
            ret += self.right.__str__(level+1)
        if self.left:
            ret += self.left.__str__(level+1)
        return ret
    
def createTree(arr):
    if arr == []:
        return None
    mid_index = len(arr) / 2
    left = arr[:mid_index]
    right = arr[mid_index+1:]
    mid = arr[mid_index]
    t = Tree(mid)
    t.left = createTree(left)
    t.right = createTree(right)
    return t
    
    
    
    
if __name__ == '__main__':
    t = createTree([1,2,3,4,5,6])
    print t

    
        
    