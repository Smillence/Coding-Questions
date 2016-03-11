''' 
SmartUQ Interview Question

Question: given a string "3:8,5,2:    5,11:22,5,7,       4,100", compress to "2:8,11:22,100"


[1:4],[2:6],7 --> [1:7]

Limitations:
1) cannot deal with bad input such as '1,3,2:::::::5,,::::,,'




Several issues to keep in mind:

1) [2:3,4] --> [2:4]
2) [2:4,5:9] --> [2:9] (use merge() function)
3) [2:4,5,6:9] --> [2:9]
4) consider the nature of matrix size, it would be better to:
	- sort lst_ints first
	- do a single loop and merge lst_ints and lst_ranges 
	(the strategy designed is similar to merge sort's)




'''
import re


# Prerequisite: string only contain ',',':',and intergers; whitespace might exist
def stringCompressor(string):
	# remove all white spaces (including TAB)
	pattern = re.compile(r'\s+')
	string = re.sub(pattern, '', string)

	# base case check
	if len(string)==0:
		return ''

	# string decomposition by ','
	lst = string.split(',')

	# remove all empty strings
	lst = filter(lambda item: item != '', lst)

	# subset lst to two sets: one contains only integers, one contains ranges such as '2:5'
	lst_ints = []
	lst_ranges = []
	for item in lst:
		if ':' in item:
			lst_ranges.append(item) # item is a string
		else:
			lst_ints.append(int(item)) # item to int

	'''CORE IMPLEMENTATION'''

	# Step 1: compress lst_ranges to format like this: [2,5,8,13]
	new_ranges = [] 
	for item in lst_ranges:

		foo = item.split(':')
		foo = map(lambda x:int(x),foo)
		Min = min(foo)
		Max = max(foo)

		# handle ranges such as '12:12', '5:5'
		if Min == Max:
			if Min not in lst_ints:
				lst_ints.append(Min)
			else:
				continue

		# initialization
		if new_ranges == []:
			new_ranges = [Min,Max]
			continue
		
		'''MAGIC COMES HERE
		1) give a list like this: 2,5,8,13 (equal to 2:5,8:13)
		2) now you need to insert 'Min', 'Max' to the list (Min<Max)
		3) for 'Min', search for i which satisfies new_ranges[i]<=Min<new_ranges[i+1].
			[What if i or i+1 is out of range? (no worry, it is handled)]
		4) for 'Max', similarly, search for j
		5) indexChange = 0
		6) if i is odd and 'Min' is not in the list: 
			insert 'Min' to position i+1
			indexChange +=1
			[What if i+1 is out of range? (no worry, it is handled)]
		   elif i is odd and 'Min' is in the list: 
			delete new_ranges[i]
			indexChange -= 1
		7) if j is odd: 
			insert 'Max' to position j+1+indexChange
			(here Max can be already in the list; since 8) will delete it by all means)
		8) if i!=j:
			delete new_ranges[i+1+indexChange],new_ranges[i+1+indexChange+1],
			...,new_ranges[j+indexChange]
		'''
		# find i and j
		i = -1
		j = -1
		i_not_found = True

		for index in range(len(new_ranges)):

			val = new_ranges[index]

			if i_not_found and Min >= val:
				i+=1
			else:
				i_not_found = False

			if Max >= val:
				j+=1
			else:
				break

		indexChange = 0
		if i % 2 == 1:
			if Min not in new_ranges:
				# Slice can be used for list insertion
				new_ranges[i+1:i+1] = [Min] # both add to front or end can be handled
				indexChange += 1
			else:
				del new_ranges[i]
				indexChange -= 1
		if j % 2 == 1:
			# the index might change by Min
			new_ranges[j+1+indexChange:j+1+indexChange] = [Max]
			
		if i!=j:
			#print new_ranges[:i+1+indexChange],new_ranges[j+indexChange+1:]
			new_ranges = new_ranges[:i+1+indexChange] + new_ranges[j+indexChange+1:]
	
			
	# Step 2: compress lst_ints 
	# (might contain duplicates; not a sorted list)
	'''
	the basic idea is: for a given int x, find index i, where new_ranges[i] < x < new_ranges[i] 
	if i is odd, add x to new_ints

	special cases such as add at the front/end should also be handled
	also cases such as [2:5,6] should also be handled
	'''
	lst_ints.sort()
	new_ints = []
	index = 0
	for item in lst_ints:
		while index < len(new_ranges):
			val = new_ranges[index]
			if item > val:
				if item - val ==1 and index%2 == 1:
					new_ranges[index] += 1
				else:
					index += 1
			elif item < val:
				if index%2 == 0:
					if new_ranges[index] - item ==1:
						new_ranges[index] -= 1
					else:
						new_ints.append(item)
				break
			else:
				break
		
		if index >= len(new_ranges):
			new_ints.append(item)

	''' for every odd element x (except the last one), if x+1 exist, delete both x and x+1
				Example: [2:5,6:12] --> [2:12]'''
	new_ranges = merge(new_ranges)
	if len(new_ints) ==0:
		return rangeConstructor(new_ranges) 
	else:
		return rangeConstructor(new_ranges) + ',' + intsConstructor(new_ints)

# Example: [2:5,6:12] --> [2:12]
def merge(lst):
	for i in range(len(lst)-2,0,-1):
		if i%2==1:
			if lst[i+1] - lst[i] == 1:
				del lst[i+1]
				del lst[i]
	return lst


# input: [0, 5, 10, 20, 30, 40]
# output: "0:5,10:20,30:40"
def rangeConstructor(lst):
	output = ''
	numPairs = len(lst) / 2
	for i in range(numPairs):
		output += str(lst[i*2]) + ':' + str(lst[i*2+1]) + ','
	output = output[:-1] # delete the last ','

	return output
# input: [0, 5, 10, 20, 30, 40]
# output: "0,5,10,20,30,40"
def intsConstructor(lst):
	output = ''
	for i in range(len(lst)):
		output += str(lst[i]) + ','
	output = output[:-1] # delete the last ','

	return output

if __name__ == '__main__':

	# print stringCompressor("")
	# print stringCompressor("  5")
	# print stringCompressor("	5") # TAB
	# print stringCompressor("5")
	# print stringCompressor("5:5")
	# print stringCompressor("3:8")
	# print stringCompressor("8:3")
	# print stringCompressor(",")
	# print stringCompressor("3:8,5,2:    5,11:22,5,7,       4,100")
	#print stringCompressor("3:8,5,2:    5,11:22,,,,,,5,7,       4,100,")

	if stringCompressor("10:20,0:5") != '0:5,10:20': 
		print stringCompressor("10:20,0:5") , '0:5,10:20'
	if stringCompressor("10:20,0:10") != '0:20':
		print stringCompressor("10:20,0:10") , '0:20' 
	if stringCompressor("10:20,0:20") != '0:20':
		print stringCompressor("10:20,0:20") , '0:20'
	if stringCompressor("10:20,0:25") != '0:25':
		print stringCompressor("10:20,0:25") , '0:25'

	if stringCompressor("10:20,10:15") != '10:20':
		print stringCompressor("10:20,10:15") , '10:20'
	if stringCompressor("10:20,10:20") != '10:20':
		print stringCompressor("10:20,10:20") , '10:20'
	if stringCompressor("10:20,10:25") != '10:25':
		print stringCompressor("10:20,10:25") , '10:25'

	if stringCompressor("10:20,15:16") != '10:20':
		print stringCompressor("10:20,15:16") , '10:20'
	if stringCompressor("10:20,15:20") != '10:20':
		print stringCompressor("10:20,15:20") , '10:20'
	if stringCompressor("10:20,15:25") != '10:25':
		print stringCompressor("10:20,15:25") , '10:25'

	if stringCompressor("10:20,20:25") != '10:25':
		print stringCompressor("10:20,20:25") , '10:25'
 
	if stringCompressor("10:20,25:30") != '10:20,25:30':
		print stringCompressor("10:20,25:30") , '10:20,25:30'

	'''print stringCompressor("10:20,30:40,0:5")
	print stringCompressor("10:20,30:40,0:10")
	print stringCompressor("10:20,30:40,0:15")
	print stringCompressor("10:20,30:40,0:20")
	print stringCompressor("10:20,30:40,0:25")
	print stringCompressor("10:20,30:40,0:30")
	print stringCompressor("10:20,30:40,0:35")
	print stringCompressor("10:20,30:40,0:40")
	print stringCompressor("10:20,30:40,0:45")

	print stringCompressor("10:20,30:40,10:15")
	print stringCompressor("10:20,30:40,10:20")
	print stringCompressor("10:20,30:40,10:25")
	print stringCompressor("10:20,30:40,10:30")
	print stringCompressor("10:20,30:40,10:35")
	print stringCompressor("10:20,30:40,10:40")
	print stringCompressor("10:20,30:40,10:45")

	print stringCompressor("10:20,30:40,15:16")
	print stringCompressor("10:20,30:40,15:20")
	print stringCompressor("10:20,30:40,15:25")
	print stringCompressor("10:20,30:40,15:30")
	print stringCompressor("10:20,30:40,15:35")
	print stringCompressor("10:20,30:40,15:40")
	print stringCompressor("10:20,30:40,15:45")

	print stringCompressor("10:20,30:40,20:25")
	print stringCompressor("10:20,30:40,20:30")
	print stringCompressor("10:20,30:40,20:35")
	print stringCompressor("10:20,30:40,20:40")
	print stringCompressor("10:20,30:40,20:45")

	print stringCompressor("10:20,30:40,25:26")
	print stringCompressor("10:20,30:40,25:30")
	print stringCompressor("10:20,30:40,25:35")
	print stringCompressor("10:20,30:40,25:40")
	print stringCompressor("10:20,30:40,25:45")
	
	print stringCompressor("10:20,30:40,30:35")
	print stringCompressor("10:20,30:40,30:40")
	print stringCompressor("10:20,30:40,30:45")

	print stringCompressor("10:20,30:40,35:36")
	print stringCompressor("10:20,30:40,35:40")
	print stringCompressor("10:20,30:40,35:45")

	print stringCompressor("10:20,30:40,40:45")

	print stringCompressor("10:20,30:40,45:50")'''

	if stringCompressor("10:20,21:30,31:40") != '10:40':
		print stringCompressor("10:20,21:30,31:40") , '10:40'

	if stringCompressor('10:20,30:50,70:90,50:70,5,9,21,29,25,90,30,91,95') != '9:21,29:91,5,25,95':
		print stringCompressor('10:20,30:50,70:90,50:70,5,9,21,29,25,90,30,91,95') , '9:21,29:91,5,25,95'
	if stringCompressor('30:40,29,30') != '29:40':
		print stringCompressor('30:40,29,30') , '29:40'
	if stringCompressor('2:4,5,6:9,10,11,18') != '2:11,18':
		print stringCompressor('2:4,5,6:9,10,11,18') , '2:11,18'

	#print stringCompressor("1,3,2:::::::5,,::::,,")
