#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000)

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

def get_sub_indices(string, sub):
	if len(sub) == 0:
		return []
	for i in range(len(string)):
		if string[i] == sub[0]:
			indices = get_sub_indices(string[i+1:], sub[1:])
			return [i] + [num + i + 1 for num in indices]
	assert True == False

def get_insertions(string, sub):
	result = []
	start = 0
	for end in get_sub_indices(string, sub):
		result += [string[start:end]]
		start = end + 1
	result += [string[start:]]
	return result

def apply_insertions(ins, sub):
	return ''.join(ins[i] + sub[i] for i in range(len(sub))) + ins[-1]

def shortest_common_supersequence(str1, str2):
	sub = longest_common_subsequence_recursive(str1, str2)
	insertions = [z[0] + z[1] for z in zip(get_insertions(str1, sub), get_insertions(str2, sub))]
	return apply_insertions(insertions, sub)
	

def main():
	with open("Input.txt") as input_file:
		strings = list(line.strip() for line in input_file)
		print(shortest_common_supersequence(strings[0], strings[1]))

main()
