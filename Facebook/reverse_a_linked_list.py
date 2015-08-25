'''
Problem: Reverse a linked list

Solution:
6 -->  8  -->2 --> 4
1) node == 6 , previous == None
2) old_next = 8, node.next = None,
[recurse]
3) node == 8, privous = 6
4) olde_next = 2, node.next = 6
[recurse]
5)....
'''

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next


def reverseNodeList(node,previous):
    
    if node.next == None:  
        node.next = previous
        return node
    else:
        old_next = node.next
        node.next = previous
        return reverseNodeList(old_next,node)
    
    

if __name__ == '__main__':
    # 6 > 8 > 2> 4
    node1 = Node(4,None)
    node2 = Node(2,node1)
    node3 = Node(8,node2)
    node4 = Node(6,node3)
    node = reverseNodeList(node4,None)
    while True:
        print node.data
        if node.next==None:break
        node = node.next    