#!/usr/bin/python
'''
Implement an algorithm to fnd the nth to last element of a singly linked list.

assume n is valid (will not exceed the length of the list)
'''

# clarification questions:
# 1) what's the return value (assume no return value)
# 2) the input is the head node.

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

# 1,2,3,4,5,6,7
# n=3, goal = 5
# 1,4
# 5, None
def foo(node,n):
    pt1 = node
    pt2 = node
    for i in range(n):
        pt2 = pt2.next
    while pt2 != None:
        pt1 = pt1.next
        pt2 = pt2.next
    return pt1
        
        
if __name__ == '__main__':
         
    print '\nTest case 6: 4 -> 2 -> 3-> 4 -> 8 -> 6 -> 6 -> 2'
    node8 = Node(2,None)
    node7 = Node(6,node8)
    node6 = Node(6,node7)
    node5 = Node(8,node6)
    node4 = Node(4,node5)
    node3 = Node(3,node4)
    node2 = Node(2,node3)
    node1 = Node(4,node2)
    print foo(node1,3).data
    print foo(node1,1).data
    print foo(node1,8).data
    '''while True:
        print node1.data
        if node1.next==None:break
        node1 = node1.next '''
    
    
    
    
    
    
    