# Assume n is a positive interger
def getNumberOfPrimes(n):
	if n<= 3:
		return n-1
	primes = [2,3]
	for num in range(4,n+1):
		finished = False
		i = 0
		while not finished:
			prime = primes[i]
			result = num / prime
			remainder = num % prime
			if remainder == 0:
				finished = True
			elif result <= prime:
				primes.append(num)
				finished = True
			i += 1
	return len(primes)

print getNumberOfPrimes(100)
