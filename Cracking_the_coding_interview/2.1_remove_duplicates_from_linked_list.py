'''
Write code to remove duplicates from an unsorted linked list. FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
'''

# clarification questions:
# 1) what's the return value (assume no return value)
# 2) the input is the head node.
# 3) will there be any circles in the linked list?
class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

# given a sequence, generate a corredpoding linked list with no circles
def NodeGenerator(seq):
    dummy = cur = Node(None,None)
    for item in seq:
        cur.next = Node(item,None)
        cur = cur.next
    return dummy.next

# solution 1: if can use a buffer, store key in a dictionary
def removeDuplicate_hash(node):
	if node == None:
		return

	hash_table = [node.data]
    
  	pre = node
	cur = node
	while cur.next != None:
		cur = cur.next
		if cur.data in hash_table:
			pre.next = cur.next
			cur.next = None
			cur = pre
		else:
			hash_table.append(cur.data)
			pre = cur




# solution 2: cannot use a buffer, scan from the head, remove duplicates after        
def removeDuplicate(node):
    if node == None:
        return
    
    val = node.data
    
    cur = node
    pre = node
    while cur.next != None:
        cur = cur.next
        if cur.data == val:
            pre.next = cur.next
            cur.next = None
            cur = pre
        else:
            pre = cur
            
    if node.next != None:        
        removeDuplicate(node.next)


''' BELOW ARE UNIT TESTS '''

def test(func):
    node = NodeGenerator([4,8,2,4])
    removeDuplicate(node)
    while True:
        if node.next==None:break
        node = node.next 
      
if __name__ == '__main__':
    print '\nTest case 1: 4 -> 8 -> 2-> 4'
    node1 = NodeGenerator([4,8,2,4])
    removeDuplicate(node1)
    while True:
        print node1.data
        if node1.next==None:break
        node1 = node1.next 
        
    print '\nTest case 2: 4 -> 4'
    node2 = Node(4,None)
    node1 = Node(4,node2)
    removeDuplicate(node1)
    while True:
        print node1.data
        if node1.next==None:break
        node1 = node1.next
        
    print '\nTest case 3: 4'
    node1 = Node(4,None)
    removeDuplicate(node1)
    while True:
        print node1.data
        if node1.next==None:break
        node1 = node1.next
        
    print '\nTest case 4: None'
    node1 = None
    print removeDuplicate(node1)
    
    print '\nTest case 5: 4 -> 2 -> 2-> 4'
    node4 = Node(4,None)
    node3 = Node(2,node4)
    node2 = Node(2,node3)
    node1 = Node(4,node2)
    removeDuplicate(node1)
    while True:
        print node1.data
        if node1.next==None:break
        node1 = node1.next        
        
    print '\nTest case 6: 4 -> 2 -> 3-> 4 -> 8 -> 6 -> 6 -> 2'
    node8 = Node(2,None)
    node7 = Node(6,node8)
    node6 = Node(6,node7)
    node5 = Node(8,node6)
    node4 = Node(4,node5)
    node3 = Node(3,node4)
    node2 = Node(2,node3)
    node1 = Node(4,node2)
    removeDuplicate_hash(node1)
    while True:
        print node1.data
        if node1.next==None:break
        node1 = node1.next
        