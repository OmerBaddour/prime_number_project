"""
1. Euclid's Algorithm

Part 1.
Function gcd takes in two numbers, calculates and returns their GCD

"""
import math

def gcd(x,y):
	
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

"""
Part 2.
Test gcd() for GCD(4278, 8602), GCD(406,555), and GCD(244, 354)

"""
if __name__ == '__main__':
	print(gcd(4278,8602))
	print(gcd(406,555))
	print(gcd(244,354))
