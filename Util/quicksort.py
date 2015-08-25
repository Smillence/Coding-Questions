# sort a list of numbers
def quicksort(lst):
	if len(lst)<=1:
	    return lst
	    
	pivot = lst[0]
	left,right = partition(lst[1:],pivot)
	return quicksort(left) + [pivot] + quicksort(right)

# lenght of lst is at least 1
def partition(lst,pivot):
    left = 0
    right = 0
    while right != len(lst):
        if lst[right] < pivot:
            lst[left],lst[right] = lst[right],lst[left]
            left += 1
        right += 1
    return lst[:left],lst[left:]


if __name__ == '__main__':
    print quicksort([6,9,2,9,10,6])
    print quicksort([2,1])