#!/usr/bin/env python3

def longest_common_subsequence(str1, str2):
	strings_not_lists = None
	if isinstance(str1, str) and isinstance(str2, str):
		strings_not_lists = True
	elif isinstance(str1, list) and isinstance(str2, list):
		strings_not_lists = False
#	assert strings_not_lists == True or strings_not_lists == False
	assert strings_not_lists == True
		
	# Initiate results table
	l1, l2 = len(str1), len(str2)
	tmp, results_table = [], []
	for i in range(l2 + 1):
		tmp.append(0)
	for i in range(l1 + 1):
		results_table.append(tmp[:])

	def longest(str1, str2):
		return str1 if len(str1) > len(str2) else str2

	# Recursive search, results are cached in results_table
	def LCS(str1, str2):
		l1, l2 = len(str1), len(str2)
		if results_table[l1][l2] != 0:
			return results_table[l1][l2]
		if 0 == l1 or 0 == l2:
			results_table[l1][l2] = '' if strings_not_lists else []
			return results_table[l1][l2]
		if str1[-1] == str2[-1]:
			results_table[l1][l2] = LCS(str1[:-1], str2[:-1]) + str1[-1]
			return results_table[l1][l2]
		else:
			results_table[l1][l2] = longest(LCS(str1, str2[:-1]), LCS(str1[:-1], str2))
			return results_table[l1][l2]

	return LCS(str1, str2)

def main():
	
	str1 = "AGCATC"#AGCAT
	str2 = "GAC"
	print(longest_common_subsequence(str1, str2))

main()
