#!/usr/bin/env python3
from collections import Counter
# Returns all DNAs as {name:string}
def read_DNAs_FASTA(input_file):
	result = {}
	name = ''
	DNAstring = ''
	for line in input_file:
		if '>' == line.strip()[0] : # Either it's the first iteration or we've just finished another DNA
			if len(name) > 0 : # It's not the first iteration
				result[name] = DNAstring
				DNAstring = ''
			name = line.strip().replace('>', '')
		else :
			DNAstring += line.strip()
	if len(DNAstring) > 0 : # We've one unfinished entry
		result[name] = DNAstring
	return result

def fact(n):
	return 1 if n < 2 else n * fact(n - 1)

def main():
	with open("Input.fasta") as input_file:
		counts = Counter(list(read_DNAs_FASTA(input_file).values())[0])
		print(fact(counts['A']) * fact(counts['G']))

main()
