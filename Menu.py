"""
////////////////////////////////////////////////////////////|
Menu containing all methods for Amazing Prime Numbers Project
////////////////////////////////////////////////////////////|

Euclid's Algorithm

Function gcd takes in two numbers, calculates and returns their GCD

"""


import math, random, csv, matplotlib.pyplot as plt

def gcd_print(x,y):
	
	a = x
	b = y
	r = None
	r_prev = None
	while(r != 0):
		q = math.floor(a/b)
		r_prev = r
		r = a - (q*b)
		print(str(a) + " = " + str(q) + "*" + str(b) + " + " + str(r))
		a = b
		b = r
	return r_prev;

def gcd(x,y):
	
	a = x
	b = y
	r = None
	r_prev = None
	while(r != 0):
		q = math.floor(a/b)
		r_prev = r
		r = a - (q*b)
		a = b
		b = r
	return r_prev;

"""
Sieve of Eratosthenes

Generates all primes up to and including n

"""


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


"""
Primality Testing


Using Trial Division

"""


def prime_test_trial(n):

	primes = sieve(math.floor(math.sqrt(n)))
	#track position
	for i in range(0,len(primes)-1):
		print(n % primes[i])
		#iterate through list of primes from 2 to sqrt(n), check for divisibility
		if(n % primes[i] == 0):
			#n is not prime
			return False
	
	#n is prime
	return True


"""
Using the Sieve of Eratosthenes

"""


def prime_test_sieve(n):

	primes = sieve(n)
	#if n is in sieve(n), we know n is prime
	#only need to check last value of output of sieve(n), as sieve(n) only returns primes less than or equal to n
	if(primes[len(primes)-1] == n):
		#n is prime
		return True
	else:
		#n is not prime
		return False


"""
Using Fermat's Little Theorem

"""


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
		return False
	else:
		return True


"""
Factorization


Using Trial Division

"""


def factor_trial(n):

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
				print(primes[i])
				exp[i] += 1
				print(exp[i])
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

"""
Using Pollard's Rho Algorithm

"""


"""
THIS IS ALL HORSESHIT

def factor_pollard_rho(n):
   
   factors = []
   store[]
   store.append() = factor_pollard_rho_helper(n)
   while(prime_test_fermat(store) == False)):
   		factor_pollard_rho_helper(temp)
     	
     



def factor_pollard_rho_helper(n):

	temp = n
	#a = random.randint(2,n-1)
	a = 2
	greatest_cd = 1
	
	counter = 0

	while(prime_test_fermat(temp) == False):
		x_prev = a
		while(greatest_cd == 1 and counter < 10):
			x = (x_prev**2 + 1) % n
			#print(str(x))
			y = (x**2 + 1) % n
			#print(str(y))
			#greatest_cd = gcd(abs(x-y),n)
			greatest_cd = gcd(abs(x-y),temp)
			#print(str(greatest_cd))
			x_prev = x
			counter += 1
		if(counter == 10):
			print("shit")
			x_prev = random.randint(2,n-1)
			counter = 0
		while(prime_test_fermat(greatest_cd) == False):
		temp /= greatest_cd
		if(temp == 1):
			counter = 0
	
	if(len(factors) == 0):
		return str(n) + " = " + str(n)
	
	factors.sort()
	#create string of factors
	factorization = ""
	for i in range(0,len(factors)):
		factorization += str(factors[i]) + " * "
	factorization = factorization[:-2]
	
	return str(n) + " = " + factorization

if __name__ == '__main__':
	#tests
	print(pollard_rho(20))
	#print(factor_pollard_rho(200))
"""

"""
Prime Distribution

Reads in file of 1 million primes, returns list of primes

"""

def get_primes(n):
	primes = []
	with open('P-1000000.csv') as millionprimes:
		csv_reader = csv.reader(millionprimes, delimiter=',')
		for i in csv_reader:
			primes.append(i[1][1:])

	millionprimes.close()
	return primes[0:n]

"""
Calculates proportion of primes that end in 1, 3, 7 and 9

"""

def proportion_of_primes(n):
	primes = get_primes(n)
	ones = 0
	threes = 0
	sevens = 0
	nines = 0
	for i in primes:
		if i[-1] == '1':
			ones += 1
		elif i[-1] == '3':
			threes += 1
		elif i[-1] == '7':
			sevens += 1
		elif i[-1] == '9':
			nines += 1

	prop1 = ones/len(primes)
	prop3 = threes/len(primes)
	prop7 = sevens/len(primes)
	prop9 = nines/len(primes)

	string1 = "The proportion of primes ending in a '1' in the first n primes is:"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '3' in the first n primes is:"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '7' in the first n primes is:"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '9' in the first n primes is:"+ str(prop9) + "\n" 

	return string1 + string3 + string7 + string9

def primes_ending_with_1_followed_by(n):
	primes = get_primes(n)
	ones = 0
	threes = 0
	sevens = 0
	nines = 0
	for i in range(len(primes)-1):
		if primes[i][-1] == '1' and primes[i+1][-1] == '1':
			ones += 1
		if primes[i][-1] == '1' and primes[i+1][-1] == '3':
			threes += 1
		if primes[i][-1] == '1' and primes[i+1][-1] == '7':
			sevens += 1
		if primes[i][-1] == '1' and primes[i+1][-1] == '9':
			nines += 1

	prop1 = ones/len(primes)
	prop3 = threes/len(primes)
	prop7 = sevens/len(primes)
	prop9 = nines/len(primes)

	string1 = "The proportion of primes ending in a '1' followed by a '1' in the first n primes is:"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '1' followed by a '3' in the first n primes is:"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '1' followed by a '7' in the first n primes is:"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '1' followed by a '9' in the first n primes is:"+ str(prop9) + "\n" 
	return string1 + string3 + string7 + string9

def primes_ending_with_3_followed_by(n):
	primes = get_primes(n)
	ones = 0
	threes = 0
	sevens = 0
	nines = 0
	for i in range(len(primes)-1):
		if primes[i][-1] == '3' and primes[i+1][-1] == '1':
			ones += 1
		if primes[i][-1] == '3' and primes[i+1][-1] == '3':
			threes += 1
		if primes[i][-1] == '3' and primes[i+1][-1] == '7':
			sevens += 1
		if primes[i][-1] == '3' and primes[i+1][-1] == '9':
			nines += 1

	prop1 = ones/len(primes)
	prop3 = threes/len(primes)
	prop7 = sevens/len(primes)
	prop9 = nines/len(primes)

	string1 = "The proportion of primes ending in a '3' followed by a '1' in the first n primes is:"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '3' followed by a '3' in the first n primes is:"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '3' followed by a '7' in the first n primes is:"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '3' followed by a '9' in the first n primes is:"+ str(prop9) + "\n" 
	return string1 + string3 + string7 + string9

def primes_ending_with_7_followed_by(n):
	primes = get_primes(n)
	ones = 0
	threes = 0
	sevens = 0
	nines = 0
	for i in range(len(primes)-1):
		if primes[i][-1] == '7' and primes[i+1][-1] == '1':
			ones += 1
		if primes[i][-1] == '7' and primes[i+1][-1] == '3':
			threes += 1
		if primes[i][-1] == '7' and primes[i+1][-1] == '7':
			sevens += 1
		if primes[i][-1] == '7' and primes[i+1][-1] == '9':
			nines += 1

	prop1 = ones/len(primes)
	prop3 = threes/len(primes)
	prop7 = sevens/len(primes)
	prop9 = nines/len(primes)

	string1 = "The proportion of primes ending in a '7' followed by a '1' in the first n primes is:"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '7' followed by a '3' in the first n primes is:"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '7' followed by a '7' in the first n primes is:"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '7' followed by a '9' in the first n primes is:"+ str(prop9) + "\n" 
	return string1 + string3 + string7 + string9

def primes_ending_with_9_followed_by(n):
	primes = get_primes(n)
	ones = 0
	threes = 0
	sevens = 0
	nines = 0
	for i in range(len(primes)-1):
		if primes[i][-1] == '9' and primes[i+1][-1] == '1':
			ones += 1
		if primes[i][-1] == '9' and primes[i+1][-1] == '3':
			threes += 1
		if primes[i][-1] == '9' and primes[i+1][-1] == '7':
			sevens += 1
		if primes[i][-1] == '9' and primes[i+1][-1] == '9':
			nines += 1

	prop1 = ones/len(primes)
	prop3 = threes/len(primes)
	prop7 = sevens/len(primes)
	prop9 = nines/len(primes)

	string1 = "The proportion of primes ending in a '9' followed by a '1' in the first n primes is:"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '9' followed by a '3' in the first n primes is:"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '9' followed by a '7' in the first n primes is:"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '9' followed by a '9' in the first n primes is:"+ str(prop9) + "\n" 
	return string1 + string3 + string7 + string9

def twin_prime_counter(n):
	primes = get_primes(n)
	twinprimes=0
	for i in range(len(primes)-1):
		if int(primes[i+1]) - int(primes[i]) == 2:
			twinprimes += 1

	return "The number of twin primes in the first n primes is: " + str(twinprimes)

def plot_pi(x,n):
	primes = get_primes(n)
	primeset = set(primes)
	x_li = []
	y_li = []
	primecount = 0
	for i in range(x):
		x_li.append(i)
		if str(i) in primeset:
			primecount += 1
		y_li.append(primecount)
	plt.plot(x_li, y_li)
	plt.ylabel('# of primes < x')
	plt.xlabel('ints < x')
	plt.show()

if __name__ == '__main__':
	print("Hello, this our menu. You can: ")
	print("Calculate the gcd of two numbers by typing ""a number1 number 2")
	print("Generate primes up to a certain number using the Sieve of Eratosthenes by typing ""b number")
	print("Test a number for primality using trial division by typing ""c number")
	print("Test a number for primality using the Sieve of Eratosthenes by typing ""d number")
	print("Test a number for primality using Fermat's Little Theorem by typing ""e number")
	print("Factor a number into its prime factors using trial division by typing ""f number")
	print("Factor a number into its prime factors using Pollard's Rho Algorithm by typing ""g number")
	print("Calculate the proportion of the first n primes that end with a 1, 3, 7, 9 by typing ""h number")
	print("Calculate the proportion of the first n primes that end with a 1 and are followed by a prime ending with a 1, 3, 7, 9 by typing ""i number")
	print("Calculate the proportion of the first n primes that end with a 3 and are followed by a prime ending with a 1, 3, 7, 9 by typing ""j number")
	print("Calculate the proportion of the first n primes that end with a 7 and are followed by a prime ending with a 1, 3, 7, 9 by typing ""k number")
	print("Calculate the proportion of the first n primes that end with a 9 and are followed by a prime ending with a 1, 3, 7, 9 by typing ""l number")
	print("Calculate the number of twin primes there are within the first n primes by typing ""m number")

	command = input("What would you like to do?")
	command = command.split(" ")
	if(command[0] == "a"):
		print(gcd(command[1],command[2]))
	if(command[0] == "b"):
		print(sieve(command[1]))
	if(command[0] == "c"):
		print(prime_test_trial(command[1]))
	if(command[0] == "d"):
		print(prime_test_sieve(command[1]))
	if(command[0] == "e"):
		print(prime_test_fermat(command[1]))
	if(command[0] == "f"):
		print(factor(command[1]))
	if(command[0] == "g"):
		print(factor_pollard_rho(command[1]))
	if(command[0] == "h"):
		print(proportion_of_primes(command[1]))
	if(command[0] == "i"):
		print(primes_ending_with_1_followed_by(command[1]))
	if(command[0] == "j"):
		print(primes_ending_with_3_followed_by(command[1]))
	if(command[0] == "k"):
		print(primes_ending_with_7_followed_by(command[1]))
	if(command[0] == "l"):
		print(primes_ending_with_9_followed_by(command[1]))
	if(command[0] == "m"):
		print(twin_prime_counter(command[1]))