#!/usr/bin/env python3
from functools import reduce
from operator import mul

def read_correspondence_table(input_file):
	result = {}
	for line in input_file:
		result[line.strip()[0:3]] = line.strip()[4:8]
	return result

def invert_correspondence_table(table):
	result = {}
	for item in table.items():
		if item[1] in result:
			result[item[1]].append(item[0])
		else:
			result[item[1]] = [item[0]]
	return result

def get_number_of_RNA_variants(prot_string, corr_table):
	inv_table = invert_correspondence_table(corr_table)
	stop_buff = len(inv_table['Stop'])
	return stop_buff * reduce(mul, map(lambda ch: len(inv_table[ch]), prot_string))

def main():
	prot_string = "MA"
	with open("Codons_proteins_table.txt", "r") as table_file:
		corr_table = read_correspondence_table(table_file)
		print(get_number_of_RNA_variants(prot_string, corr_table) % 10**6)

main()
