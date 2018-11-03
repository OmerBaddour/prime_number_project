"""
2. Sieve of Eratosthenes

Part 1.
Generating all primes up to and including n

"""

import math

def sieve(n):

	primes = []

	#creating a list from 2 to n
	for x in range(0,n-2):
		primes.append(x+2)

	#for all numbers from 2 to floor(sqrt(n)), remove all multiples of each number (y) from 2 to floor(n/y)
	for x in range(2,math.floor(math.sqrt(n))+1):
		for y in range(2,math.floor(n/x)+1):
			if (y*x) in primes:
				primes.remove(y*x) 

	return primes

if __name__ == '__main__':
	print(sieve(100))
