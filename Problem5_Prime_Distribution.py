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


if __name__ == '__main__':
	proportion_of_primes()