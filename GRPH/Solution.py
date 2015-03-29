#!/usr/bin/env python3

from functools import reduce
import operator

# Returns all DNAs as {name:string}
def read_DNAs_FASTA(input_file):
	result = {}
	name = ''
	DNAstring = ''
	for line in input_file:
		if '>' == line.strip()[0] :# Either it's the first iteration or we've just finished another DNA
			if len(name) > 0 : # It's not the first iteration
				result[name] = DNAstring
				DNAstring = ''
			name = line.strip().replace('>', '')
		else :
			DNAstring += line.strip()
	if len(DNAstring) > 0 : # We've one unfinished entry
		result[name] = DNAstring
	return result

def is_overlapped(string1, string2, overlap):
	return reduce(lambda x,y : x and y, map(operator.eq, string1[-overlap:], string2[:overlap]))

def get_adjacency_list(DNAs, overlap):
	result = {}
	for first in DNAs.keys():
		for second in DNAs.keys():
			if first == second :
				continue
			if is_overlapped(DNAs[first], DNAs[second], 3) :
				if first in result:
					result[first].append(second)
				else:
					result[first] = [second]
	return result

def print_adjacency_list(adjlist, output_file):
	for first in adjlist.keys():
		for second in adjlist[first]:
			print(first, second, file=output_file)

def main():
	with open("Input.txt", "r") as input_file:
		DNAs = read_DNAs_FASTA(input_file)
		with open("Output.txt", "w") as output_file:
			print_adjacency_list(get_adjacency_list(DNAs, 3), output_file)

main()
