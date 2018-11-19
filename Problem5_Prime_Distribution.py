import math
import csv
import matplotlib.pyplot as plt

"""
reads in file of 1 million primes, returns list of primes
"""

def get_primes():
	primes = []
	with open('P-1000000.csv') as millionprimes:
		csv_reader = csv.reader(millionprimes, delimiter=',')
		for i in csv_reader:
			primes.append(i[1][1:])

	millionprimes.close()
	return primes

"""
Calculates proportion of primes that end in 1, 3, 7 and 9
"""

def proportion_of_primes():
	primes = get_primes()
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

	string1 = "The proportion of primes ending in a '1':"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '3':"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '7':"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '9':"+ str(prop9) + "\n" 

	return string1 + string3 + string7 + string9

def primes_ending_with_1_followed_by():
	primes = get_primes()
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

	string1 = "The proportion of primes ending in a '1' followed by a '1':"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '1' followed by a '3':"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '1' followed by a '7':"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '1' followed by a '9':"+ str(prop9) + "\n" 
	return string1 + string3 + string7 + string9

def primes_ending_with_3_followed_by():
	primes = get_primes()
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

	string1 = "The proportion of primes ending in a '3' followed by a '1':"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '3' followed by a '3':"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '3' followed by a '7':"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '3' followed by a '9':"+ str(prop9) + "\n" 
	return string1 + string3 + string7 + string9

def primes_ending_with_7_followed_by():
	primes = get_primes()
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

	string1 = "The proportion of primes ending in a '7' followed by a '1':"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '7' followed by a '3':"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '7' followed by a '7':"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '7' followed by a '9':"+ str(prop9) + "\n" 
	return string1 + string3 + string7 + string9

def primes_ending_with_9_followed_by():
	primes = get_primes()
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

	string1 = "The proportion of primes ending in a '9' followed by a '1':"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '9' followed by a '3':"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '9' followed by a '7':"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '9' followed by a '9':"+ str(prop9) + "\n" 
	return string1 + string3 + string7 + string9

def twin_prime_counter():
	primes = get_primes()
	twinprimes=0
	for i in range(len(primes)-1):
		if int(primes[i+1]) - int(primes[i]) == 2:
			twinprimes += 1

	return "The number of twin primes is: " + str(twinprimes)

def plot_pi(x):
	primes = get_primes()
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
	print(proportion_of_primes())
	print(primes_ending_with_1_followed_by())
	print(primes_ending_with_3_followed_by())
	print(primes_ending_with_7_followed_by())
	print(primes_ending_with_9_followed_by())
	print(twin_prime_counter())
	plot_pi(300000)