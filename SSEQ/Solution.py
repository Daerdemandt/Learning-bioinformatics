#!/usr/bin/env python3

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

def get_sub_indices(string, sub):
	if len(sub) == 0:
		return []
	for i in range(len(string)):
		if string[i] == sub[0]:
			indices = get_sub_indices(string[i+1:], sub[1:])
			return [i] + [num + i + 1 for num in indices]
	assert True == False

def main():
	with open("Input.fasta") as input_file:
		strings = read_fasta_strings(input_file)
		print(' '.join(str(index+1) for index in get_sub_indices(strings[0], strings[1])))
main()
