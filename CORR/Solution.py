#!/usr/bin/env python3
from operator import ne
from functools import reduce
from bisect import bisect
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


def reverse_compliment(string):
	def compliment(x):
		return {'A':'T', 'T':'A', 'C':'G', 'G':'C'}[x]
	return ''.join(compliment(x) for x in string[::-1])

def divide_strings(strings):
	strings_complimented = strings + list(map(reverse_compliment, strings))
	loners_complimented = set(item[0] for item in Counter(strings_complimented).items() if item[1] == 1)
	incorrect_reads = loners_complimented & set(strings)
	correct_reads = set(strings_complimented) - loners_complimented
	return correct_reads, incorrect_reads

def hamming_distance(s1, s2):
	return sum(map(ne, s1, s2))

def match_incorrect_reads(correct_reads, incorrect_reads):
	search_base = sorted(correct_reads)
	length = len(search_base)
	result = {}
	divergents = set()
	def fast_correction_search(read):
		def is_at(read, index):
			if index >= length or index <= 0:
				return False
			return 1 == hamming_distance(read, search_base[index])

		def get_correction(read, index):
			if is_at(read, index - 1):
				return search_base[index - 1]
			if is_at(read, index):
				return search_base[index]

		index = bisect(search_base, read)
		correction = get_correction(read, index)
		if correction:
			return correction
		else:
			revc_read = reverse_compliment(read)
			index = bisect(search_base, revc_read)
			revc_correction = get_correction(revc_read, index)
			if revc_correction:
				return reverse_compliment(revc_correction)

	for read in incorrect_reads:
		correction = fast_correction_search(read)
		if not correction:
			calculated_base = {string:hamming_distance(read, string) for string in search_base} # method is ugly but failsafe
			correction = list(calculated_base.keys())[list(calculated_base.values()).index(1)]
		result[read] = correction
	return result

def print_corrections(corrections, output_file):
	for broken_read in corrections:
		print(broken_read + '->' + corrections[broken_read], file=output_file)


def main():
	with open("Input.fasta") as input_file:
		strings = list(read_DNAs_FASTA(input_file).values())
		errata = match_incorrect_reads(*divide_strings(strings))
		with open("Output.txt", "w") as output_file:
			print_corrections(errata, output_file)

main()
