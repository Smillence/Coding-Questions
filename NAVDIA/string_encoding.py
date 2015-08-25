''' 
NVIDIA Interview Question
ECS Spring Career Fair

Question: String Encoding.
Description: AAABBBBBEEAADDDDCCCC --> 3A5B2E2A4D4C

'''

def stringEncoder(string):
	if len(string)==0:
		return None
	char = string[0]
	count = 0
	for index in range(len(string)):
		if string[index] == char:
			count += 1
		else:
			return str(count)+char+stringEncoder(string[index:])
	return str(count)+char

if __name__ == '__main__':
	print stringEncoder('AAABBBBBEEAADDDDCCCC')