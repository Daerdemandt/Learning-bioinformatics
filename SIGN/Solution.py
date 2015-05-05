#!/usr/bin/env python3
from math import factorial
from itertools import permutations

n = 2

def signed_permutations(n):
	for perm in permutations(range(1, n + 1)):
		for num in range(2 ** n):
			flags = '{:b}'.format(num).zfill(n)
			yield [perm[i] if '0' == flags[i] else -perm[i] for i in range(n)]
def main():
	with open("Output.txt", "w") as output_file:
		print(factorial(n) * 2 ** n, file=output_file)
		for s_perm in signed_permutations(n):
			print(' '.join(str(num) for num in s_perm), file=output_file)

main()
