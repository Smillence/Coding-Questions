''' 
NVIDIA Interview Question
ECS Spring Career Fair

Question: sort a linked list

'''

class Node:
	def __init__(self,data,next):
		self.data = data
		self.next = next


def sortNodeList(node):
	'''ADD YOUR CODE HERE'''
	if node==None:return None
	if node.next==None:return None

	lst = [node]
	head = node
	while head.next != None:
		lst.append(head.next)
		head = head.next

	lst = mergeSort(lst)
	for index in range(len(lst)-1):
		lst[index].next = lst[index+1]
	lst[len(lst)-1].next=None
	return lst[0]

def mergeSort(lst):
	length = len(lst)
	if length < 2: return lst
	lst1 = mergeSort(lst[:length/2])
	lst2 = mergeSort(lst[length/2:])
	return merge(lst1,lst2)

def merge(lst1,lst2):
	if len(lst1) == 0: return lst2
	if len(lst2) == 0: return lst1
	if lst1[0].data <= lst2[0].data:
		return [lst1[0]] + merge(lst1[1:],lst2)
	else:
		return [lst2[0]] + merge(lst2[1:],lst1)


if __name__ == '__main__':
	node1 = Node(4,None)
	node2 = Node(2,node1)
	node3 = Node(8,node2)
	node4 = Node(6,node3)
	node = sortNodeList(node4)
	while True:
		print node.data
		if node.next==None:break
		node = node.next





