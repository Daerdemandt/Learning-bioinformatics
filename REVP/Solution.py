#!/usr/bin/env python3

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


def compliment(x):
	return {'A':'T', 'T':'A', 'C':'G', 'G':'C'}[x]

def partial_check_for_revp(string, position, offset):
	if (position < offset) or (position + 1 + offset == len(string)):
		return False
	return string[position - offset] == compliment(string[position + 1 + offset])

def get_revp_size(string, position, limit):
	offset = 0
	while (partial_check_for_revp(string, position, offset)):
		offset += 1
		if offset * 2 == limit:
			break
	return offset * 2

def get_revps(string, low_limit, high_limit):
	for i in range(len(string)):
		new_revp_size = get_revp_size(string, i, high_limit)
		if (new_revp_size >= low_limit):
			for j in range(low_limit, new_revp_size + 2, 2):
				yield (i - j // 2 + 2, j) #position and size
def main():
	with open("Input.fasta", "r") as input_file:
		DNA = list(read_DNAs_FASTA(input_file).values())[0]
		for revp in get_revps(DNA, 4, 12):
			print (revp[0], revp[1])

main()
