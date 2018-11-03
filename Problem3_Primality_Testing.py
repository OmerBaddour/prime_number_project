"""
3. Primality Testing

Part 1.
Why would I do without Sieve boi?

"""

"""
Part 2.
Assuming between is inclusive of sqrt(n)

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

def prime_test_sieve(n):

	primes = sieve(n)
	solutions = []
	for x in range(2,math.floor(math.sqrt(n))+1):
		if((n % x == 0) and (x in primes)):
			solutions.append(x)

	if(len(solutions) > 0):
		return(str(solutions) + " = The set of prime(s) between 2 and sqrt(" + str(n) + ") which divide " + str(n))
	else:
		return("There are no primes between 2 and sqrt(" + str(n) + ") which divide " + str(n))

if __name__ == '__main__':
	print(prime_test_sieve(30))