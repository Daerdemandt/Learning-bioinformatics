#!/usr/bin/env python3
from functools import reduce
from operator import mul
from collections import Counter

def read_fasta_string(input_file):
	multistring = input_file.readlines()[1:]
	return ''.join(string.strip() for string in multistring)

def partial_permutations(a, b):
	a, b = max(a, b), min(a, b)
	return reduce(mul, range(1 + a - b, a + 1))

def main():
	with open("Input.fasta") as input_file:
		counts = Counter(read_fasta_string(input_file))
		print(partial_permutations(counts['A'], counts['U']) * partial_permutations(counts['C'], counts['G']))

main()
