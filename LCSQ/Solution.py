#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

def read_fasta_strings(input_file):
	result = []
	name = ''
	DNAstring = ''
	for line in input_file:
		if '>' == line.strip()[0] : # Either it's the first iteration or we've just finished another DNA
			if len(name) > 0 : # It's not the first iteration
				result += [DNAstring]
				DNAstring = ''
			name = line.strip().replace('>', '')
		else :
			DNAstring += line.strip()
	if len(DNAstring) > 0 : # We've one unfinished entry
		result += [DNAstring]
	return result


def longest_common_subsequence_recursive(seq1, seq2):
	strings_not_lists = None
	if isinstance(seq1, str) and isinstance(seq2, str):
		strings_not_lists = True
	elif isinstance(seq1, list) and isinstance(seq2, list):
		strings_not_lists = False
	assert strings_not_lists == True or strings_not_lists == False
		
	# Initiate results table
	l1, l2 = len(seq1), len(seq2)
	tmp, results_table = [], []
	for i in range(l2 + 1):
		tmp.append(None)
	for i in range(l1 + 1):
		results_table.append(tmp[:])

	def longest(seq1, seq2):
		return seq1 if len(seq1) > len(seq2) else seq2

	# Recursive search, results are cached in results_table
	def LCS(seq1, seq2):
		l1, l2 = len(seq1), len(seq2)
		if results_table[l1][l2] != None:
			pass
		elif 0 == l1 or 0 == l2:
			results_table[l1][l2] = '' if strings_not_lists else []
		elif seq1[-1] == seq2[-1]:
			if strings_not_lists:
				results_table[l1][l2] = LCS(seq1[:-1], seq2[:-1]) + seq1[-1]
			else:
				results_table[l1][l2] = LCS(seq1[:-1], seq2[:-1])
				results_table[l1][l2].append(seq1[-1])
		else:
			results_table[l1][l2] = longest(LCS(seq1, seq2[:-1]), LCS(seq1[:-1], seq2))
		return results_table[l1][l2][:]

	return LCS(seq1, seq2)
# end of longest_common_subsequence_recursive


def main():
	with open("Input.fasta") as input_file:
		strings = read_fasta_strings(input_file)
		print(longest_common_subsequence_recursive(strings[0], strings[1]))

main()
