'''
Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.

EXAMPLE

Input: the node 'c' from the linked list a->b->c->d->e

Result: nothing is returned, but the new linked list looks like a->b->d->e
'''

# clarification questions:
# 1) what does middle mean? i think this is not useful
# 2) can it be in the head? (yes)
# 3) can it be in the tail? (no)
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

def foo(node_middle):
    while node_middle.next != None:
        node_middle.data = node_middle.next.data
        if node_middle.next.next != None:
            node_middle = node_middle.next
        else:
            node_middle.next = None
            
    
if __name__ == '__main__':

    
    print '\nTest case 6: 4 -> 2 -> 3-> 4 -> 8 -> 6'
    node6 = Node(6,None)
    node5 = Node(8,node6)
    node4 = Node(4,node5)
    node3 = Node(3,node4)
    node2 = Node(2,node3)
    node1 = Node(4,node2)
    foo(node4)
    while True:
        print node1.data
        if node1.next==None:break
        node1 = node1.next 
    
    
    
    
    
    
    