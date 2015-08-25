'''
Given a string, remove all 'b's and duplicate all 'a's. 

'''

def foo(string):
	length = len(string)
	for i in range(length-1,-1,-1):
		char = string[i]
		if char == 'b':
			string = string[:i]+string[i+1:]
		elif char == 'a':
			string = string[:i]+'a'+string[i:]
	return string



if __name__ == '__main__':
	print foo('aabbbssbbbsaasf')#aaaasssaaaasf