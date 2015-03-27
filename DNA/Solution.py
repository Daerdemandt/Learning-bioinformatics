#!/usr/bin/env python

from collections import Counter

# Counting DNA Nucleotides

with open("Input.txt", "r") as input_file:
	counts = Counter(input_file.readline().strip())
	print(counts['A'], counts['C'], counts['G'], counts['T'])
