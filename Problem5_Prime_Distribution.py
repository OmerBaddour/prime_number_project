import math
import csv

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

	proportions = []
	prop1 = ones/len(primes)
	prop3 = threes/len(primes)
	prop7 = sevens/len(primes)
	prop9 = nines/len(primes)

	string1 = "The proportion of primes ending in a '1':"+ str(prop1) + "\n"  
	string3 = "The proportion of primes ending in a '3':"+ str(prop3) + "\n" 
	string7 = "The proportion of primes ending in a '7':"+ str(prop7) + "\n"  
	string9 = "The proportion of primes ending in a '9':"+ str(prop9) + "\n" 

	return string1 + string3 + string7 + string9



if __name__ == '__main__':
	print(proportion_of_primes())