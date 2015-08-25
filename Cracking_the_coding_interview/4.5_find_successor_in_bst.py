'''
4.5
Write an algorithm to find the 'next' node (i.e., in-order successor) of a given node in a binary search tree where each node has a link to its parent.
'''

# clarification quesitons:
# 1) so it means thers is a bi-directory link? (yes)
# 2) if there does not exist such next node, return None? (yes)
# 3) a binary search tree is all left subnodes are smaller and all right subnodes are larger? (yes)


class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.parent = None
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
    t = TreeNode(mid)
    t.left = createTree(left)
    t.right = createTree(right)
    if t.left:
        t.left.parent = t
    if t.right:
        t.right.parent = t
    return t

# algorithm:
'''
if node.right does not exist:
    if parent exist and parent.data > node.data:
        return parent
    else:
        return None
else:
    go to node.right and continue to find node.right.left.left.left.....
    return the leftmost found one
'''
def findSucessor(node):
    if not node.right:
        cur = node.parent
        while cur:
            if cur.data > node.data:
                return cur
            else:
                cur = cur.parent
        return None
    else:
        cur = node.right
        while cur.left:
            cur = cur.left
        return cur
            
    
import copy    
if __name__ == '__main__':
    t = createTree([1,2,3,4,5,6])
    print t
    print findSucessor(t).data
    print findSucessor(t.left).data
    print findSucessor(t.right)
    print findSucessor(t.right.left).data
    print findSucessor(t.left.left).data
    print findSucessor(t.left.right).data

    
        
    