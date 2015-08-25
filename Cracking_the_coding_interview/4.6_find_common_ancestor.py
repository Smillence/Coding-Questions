'''
4.6
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
'''
'''
If this were a binary search tree, we could do a modified find on the two nodes and see where the paths diverge. Unfortunately, this is not a binary search tree, so we much try other approaches.
'''
# clarification quesitons:
# 1) does each node has a link to its parent? (yes)
# 2) the first common ancestor means the deepest ancestor? I mean the first common ancestor should always be the root (yes, the deepest)
# 3) the node itself is also its ancestor? (yes)

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
# modified bfs

def findCommonAncestor(n1,n2):
    frontier = [(n1,n1)]
    explored = set()
    while frontier:
        cur = frontier.pop(0)        
        cur_node = cur[0]
        explored.add(cur_node)
        common_ancestor = cur[1]
        
        if cur_node == n2:
            return common_ancestor
        if cur_node.parent and cur_node.parent not in explored:
            frontier.append((cur_node.parent,cur_node.parent))
        if cur_node.left and cur_node.left not in explored:
            frontier.append((cur_node.left,common_ancestor))
        if cur_node.right and cur_node.right not in explored:
            frontier.append((cur_node.right,common_ancestor))
                        
                            
import copy    
if __name__ == '__main__':
    t = createTree([1,2,3,4,5,6])
    print t
    n = []
    n4 = t
    n2 = t.left
    n6 = t.right
    n1 = t.left.left
    n3 = t.left.right
    n5 = t.right.left
    n = [n1,n2,n3,n4,n5,n6]
    
    for i in range(len(n)-1):
        for j in range(i+1,len(n)):
            print i+1,j+1,' :',
            print findCommonAncestor(n[i],n[j]).data
    
    

    
        
    