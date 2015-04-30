#!/usr/bin/env python3
from functools import reduce
from operator import mul

a, b = 21, 7

def main():
	print(reduce(mul, range(1 + a - b, a + 1)) % 10**6)
	
main()
