#Input: a list of numbers
#Output: a sorted list
def mergesort(lst):
	n = len(lst)
	if n>1:
		return merge(mergesort(lst[:n/2]),mergesort(lst[n/2:]))
	else:
		return lst

def merge(lst1,lst2):
	k = len(lst1)
	l = len(lst2)
	if k==0:
		return lst2
	if l==0:
		return lst1
	if lst1[0] <= lst2[0]:
		return [lst1[0]] + merge(lst1[1:],lst2)
	else:
		return [lst2[0]] + merge(lst1,lst2[1:])


if __name__ == '__main__':
	print mergesort([10,2,5,3,7,13,1,6])
