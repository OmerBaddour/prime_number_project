"""
2. Sieve of Eratosthenes

Part 1.
Generating all primes up to and including n

Populate a set of numbers p from 2 to n incrementing by 1
for each number y < math.floor(sqrt(n))
set y = numbers 1 to n incrementing by y
p = p - y
return p

"""

import math

def sieve(n):

	primes = []

	#creating a list from 2 to n
	for x in range(0,n-2):
		primes[x] = x+2

	for x in range(2,math.floor(math.sqrt(n))):
		for y in range(2,math.floor(n/y)):
			primes.remove(y*x) 

	return primes

if __name__ == '__main__':
	print(sieve(100))