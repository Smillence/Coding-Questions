'''
2.5
Given a circular linked list, implement an algorithm which returns node at the begin- ning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
EXAMPLE
input: A -> B -> C -> D -> E -> C [the same C as earlier]
output: C
'''
import copy

class Node:
    def __init__(self,data,Next):
        self.data = data
        self.Next = Next
    def __str__(self):
        output = ''
        while self!=None:
            output += str(self.data) + '->'
            self = self.Next
        return output[:-2]

    
# clarification question:
# 1) how many circles? (assume one)
    
# solution 1:
# simply use a hash-table / dict to store the address of each node
# when found a dubplicate, a circle is found
def findThatCircle_1(node):
    explored = set()
    while node != None:
        if node not in explored:
            explored.add(node)
            node = node.Next
        else:
            return node
    
    
# solution 2: do not use hash-table to store    
#  Alg design:
# a slow pointer and a fast pointer both start at the same time at the head
# fast goes 2 steps a time, slow goes 1 step
# say the length of none-circle part is x, the circle part is y
# if the first collision happends in t1, we know x <= t1 <= x+y
# if the second collision happends in t2, we know t2 >= x+y
# we can also know y = t2-t1
# Thus, the only thing we want to know is the length of x

# call foo(head,t1)

# function foo(head,tail):
# if head == tail:
#    return head # circle location found
# mid = head + tail / 2
# cut off at mid
# start from mid.Next, try to find the end
# # each round the range shrink half size
# if not found after t2 time, terminate the loop
#     call function foo(mid.Next,tail) recursively
# else:
#     paste mid with mid.Next
#     call function foo(head,mid.Next) recursively
#

#solution 3 (from the book):
'''
If we move two pointers, one with speed 1 and another with speed 2, they will end up meeting if the linked list has a loop. Why? Think about two cars driving on a trackthe faster car will always pass the slower one!

The tricky part here is finding the start of the loop. Imagine, as an analogy, two people rac- ing around a track, one running twice as fast as the other. If they start off at the same place, when will they next meet? They will next meet at the start of the next lap.

Now, let's suppose Fast Runner had a head start of k meters on an n step lap. When will they next meet? They will meet k meters before the start of the next lap. (Why? Fast Runner would have made k + 2(n - k) steps, including its head start, and Slow Runner would have made n - k steps. Both will be k steps before the start of the loop.)

Now, going back to the problem, when Fast Runner (n2) and Slow Runner (n1) are moving around our circular linked list, n2 will have a head start on the loop when n1 enters. Specifi- cally, it will have a head start of k, where k is the number of nodes before the loop. Since n2 has a head start of k nodes, n1 and n2 will meet k nodes before the start of the loop.

So, we now know the following:
1. Head is k nodes from LoopStart (by definition).
2. MeetingPoint for n1 and n2 is k nodes from LoopStart (as shown above).

Thus, if we move n1 back to Head and keep n2 at MeetingPoint, and move them both at the same pace, they will meet at LoopStart.
'''
    
    
    

if __name__ == '__main__':
    node5 = Node(5,None)
    node4 = Node(4,node5)
    node3 = Node(3,node4)
    node2 = Node(2,node3)
    node1 = Node(1,node2)
    node5.Next = node3
    print findThatCircle_1(node1).data
