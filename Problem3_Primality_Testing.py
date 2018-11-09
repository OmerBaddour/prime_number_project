"""
3. Primality Testing

Part 1.
Check if a number is prime using Trial Division.

"""
import math 

#can delete if scope of problem 2 is sufficient
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
#end potential deletion

def prime_test_trial(n):

	primes = sieve(math.floor(math.sqrt(n)))
	#track position
	for i in range(0,len(primes)-1):
		print(n % primes[i])
		#iterate through list of primes from 2 to sqrt(n), check for divisibility
		if(n % primes[i] == 0):
			return(str(n) + " is not prime.")
		
	return(str(n) + " is prime.")

"""
Part 2.
Check if a number is prime using the Sieve of Eratosthenes.

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

def prime_test_sieve(n):

	primes = sieve(n)
	#if n is in sieve(n), we know n is prime
	#only need to check last value of output of sieve(n), as sieve(n) only returns primes less than or equal to n
	if(primes[len(primes)-1] == n):
		return(str(n) + " is prime.")
	else:
		return(str(n) + " is not prime.")


"""
Part 3. 
Check if a number is prime using Fermat's Little Theorem.

"""

import random

def prime_test_fermat(p):

	prime = True
	#in case we get a Fermat liar, repeat 3 times
	#now very unlikely to yield a false positive
	repeats = 0

	while(prime and repeats < 3):
		result = 1
		#random choice of alpha
		alpha = random.randint(2,p-1)
		#array to store values of repeated squares
		rept_sqrs = [alpha]
		exp = 2

		#populate array containing repeated squares of alpha (mod p)
		while(exp < p):
			rept_sqrs.append(rept_sqrs[len(rept_sqrs)-1]**2 % p)
			exp *= 2

		#calculate alpha^(p-1) (result)
		#want to factor alpha^(p-1) using repeated squares of alpha
		temp = p-1
		index = len(rept_sqrs) - 1
		while(index >= 0):
			if(temp >= 2**index):
				result *= rept_sqrs[index]
				temp -= 2**index
			else:
				index -= 1

		#check if alpha^(p-1) is congruent to 1 (mod p)
		if(result % p != 1):
			prime = False
		repeats += 1;

	if(not prime):
		return(str(p) + " is not prime.")
	else:
		return(str(p) + " is prime.")

if __name__ == '__main__':
	#tests
	print(prime_test_trial(2222))
	print(prime_test_sieve(101))
	print(prime_test_fermat(2222222222))