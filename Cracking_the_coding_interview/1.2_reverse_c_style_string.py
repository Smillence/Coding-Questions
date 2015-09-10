'''
Write code to reverse a C-Style String. (C-String means that 'abcd' is 
    represented as five characters, including the null character.)


In C and C++, strings are typically represented as char arrays that have a null 
terminator. A null terminator means that the string ends with a '\0' character 
(which has ASCII code 0)

It is almost the same as revert a linked list

'''


# clarification questions:
# 1) input is a string ending with '\0'
# 2) i cannot use .reverse()

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
    
def reverseNodeListNonRecursive(node):
    if not node:
        return None
    rest, node.next = node.next, None
    while rest:
        rest.next, node, rest = node, rest, rest.next
    return node  

# the trick here is to add a null char at the beginning of the string and use
# the same reverting a linked list method to do it; after the reverting, just
# delete the leading null char will get the correct result
def reverseCStyleString(c_str):
    c_str = Node('\0',c_str)
    return reverseNodeListNonRecursive(c_str).next

if __name__ == '__main__':
    # 'abc\0'
    node1 = Node('\0',None)
    node2 = Node('c',node1)
    node3 = Node('b',node2)
    node4 = Node('a',node3)
    node = reverseCStyleString(node4)
    while True:
        print node.data
        if node.next==None:break
        node = node.next 
