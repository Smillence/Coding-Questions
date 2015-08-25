'''
4.4
Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (i.e., if you have a tree with depth D, you'll have D linked lists).
'''

# clarification quesitons:
# 1) input a tree, output a list of lists? (yes)
# 2) the root node depth is 1? (yes)
# 3) input is not None? (yes)
# 4) the linked list tail can be the leftmost, head can be the rightmost? (yes)


class TreeNode:
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
    t = TreeNode(mid)
    t.left = createTree(left)
    t.right = createTree(right)
    return t

class Node:
    def __init__(self,data,Next):
        self.data = data
        self.Next = Next

# algorithm: use BFS
def createLinkedLists(root):
    frontier = [(root,1)]
    output = []
    while frontier:
        cur = frontier.pop(0)

        curDepth = len(output)

        if cur[1] > curDepth:
            output.append(Node(cur[0],None))
            curDepth +=1
        else:
            tail = output[curDepth-1]
            head = Node(cur[0],tail)         
            output[curDepth-1] = head
        if cur[0].left != None:
            frontier.append((cur[0].left,curDepth+1))
        if cur[0].right != None:
            frontier.append((cur[0].right,curDepth+1))
    return output
            
    
import copy    
if __name__ == '__main__':
    t = createTree([1,2,3,4,5,6])
    print t
    lst = createLinkedLists(t)
    for node in lst:
        node = copy.deepcopy(node)
        output = ''
        while node != None:
            treeNode = node.data
            output += str(treeNode.data) + ' '
            node = node.Next
        print output

    
        
    