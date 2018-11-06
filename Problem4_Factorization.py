"""
4. Prime Factorization

Part 1.
Implementing a prime factorization algorithm using trail division

"""

import math 

#can delete if scope of problem 2 is sufficient
def sieve(n):

	primes = []

	#creating a list from 2 to n
	for x in range(0,n-1):
		primes.append(x+2)

	#for all numbers from 2 to floor(sqrt(n)), remove all multiples of each number (y) from 2 to floor(n/y)
	for x in range(2,math.floor(math.sqrt(n))+1):
		for y in range(2,math.floor(n/x)+1):
			if (y*x) in primes:
				primes.remove(y*x) 

	return primes
#end potential deletion

def factor(n):

	primes = sieve(n)
	if(primes[len(primes)-1] == n):
		return n
	else:
		#store exponents of each prime in primes needed to make n
		exp = []
		temp = n
		#track position
		i = 0
		while(temp != 1):
			exp.append(0)
			while(temp % primes[i] == 0):
				exp[i] += 1
				temp /= primes[i]
			i += 1

		#create string of factors
		factorization = ""
		for i in range(0,len(exp)):
			while(exp[i] > 0):
				factorization += str(primes[i]) + " * "
				exp[i] -= 1
		factorization = factorization[:-2]
		
		return str(n) + " = " + factorization

if __name__ == '__main__':
	#tests
	print(factor(800))
