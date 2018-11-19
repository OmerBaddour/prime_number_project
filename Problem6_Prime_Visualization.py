import numpy as np
import matplotlib.pyplot as plt
import math
import csv

def get_primes():
	primes = []
	with open('P-1000000.csv') as millionprimes:
		csv_reader = csv.reader(millionprimes, delimiter=',')
		for i in csv_reader:
			primes.append(i[1][1:])

	millionprimes.close()
	return primes

def visualize(x):
	primes = get_primes()
	primeset = set(primes)
	arr = np.zeros((int(math.sqrt(int(x))),int(math.sqrt(int(x)))), dtype=int)
	for i in range(int(math.sqrt(int(x)))):
		for j in range(int(math.sqrt(int(x)))):
			num = i*int(math.sqrt(int(x)))+j
			if str(num) in primeset:
				arr[i,j] = 1;

	plt.imshow(arr)
	plt.show()

if __name__ == '__main__':
	visualize(1000000)
