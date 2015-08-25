'''
2.4

You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE 

Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)

Output: 8 -> 0 -> 8
'''

# clarification questions:
# 1) what does middle mean? i think this is not useful
# 2) can it be in the head? (yes)
# 3) can it be in the tail? (no)
# 4) what does reverse order mean? 3 -> 1 -> 5 is 513? (yes)

class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
    def __str__(self):
        output = ''
        while True:
            output += str(self.data) + ' '
            if self.next==None:
                break
            self = self.next 
        return output

# solution 1:
# 1)convert two linked list to two numbers
# 2)add to numbers
# 3)convert the sum to a linked list
def foo(node1,node2):
    num1 = node2num(node1)
    num2 = node2num(node2)
    return num2node(num1+num2)

# input: 6->8
# output: 86
def node2num(node):
    
    output = 0
    power = 0
    while node != None:
        output += node.data * (10**power)
        power += 1
        node = node.next
    return output
 
# input: 86
# output: 6->8
def num2node(num):
    head = None
    pre = None
    while num != 0:
        data = num % 10        
        node = Node(data,None)
        
        if head == None:
            head = node
        else:
            pre.next = node
        pre = node
        num = num / 10
    return head

# solution 2 (better):
# don't need to convert to numbers first
# simply add digit one by one from the tails just like what we did in our primary school's math class
def foo2(node1,node2):
    node3 = None
    pre = None
    carry = 0
    while node1 != None or node2 !=None:
        if node1 != None:
            carry += node1.data
            node1 = node1.next
        if node2 != None:
            carry += node2.data
            node2 = node2.next
        node = Node(carry%10,None)
        carry = carry/10
        
        if node3 == None:
            node3 = node
        else:
            pre.next = node
        pre = node
    return node3
    
if __name__ == '__main__':
    
    print '\nTest case 1: 4 -> 2 -> 3-> 4 -> 8 -> 6'
    node6 = Node(6,None)
    node5 = Node(8,node6)
    node4 = Node(4,node5)
    node3 = Node(3,node4)
    node2 = Node(2,node3)
    node1 = Node(4,node2)
    print node4
    print node6
    print foo(node4,node6)
    print foo2(node4,node6)
    
    
    
    
    
    
    