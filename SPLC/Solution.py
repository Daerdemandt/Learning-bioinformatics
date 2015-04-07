#!/usr/bin/env python3

def remove_introns(DNA, introns):
	for intron in introns:
		DNA = DNA.replace(intron, '')
	return DNA

def make_codons_table(): # by LudditeCyborg
	bases = ['T', 'C', 'A', 'G']
	codons = [a+b+c for a in bases for b in bases for c in bases]
	amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
	return dict(zip(codons, amino_acids))

def read_DNAs_FASTA(input_file):
	result = []
	name = ''
	DNAstring = ''
	for line in input_file:
		if '>' == line.strip()[0] : # Either it's the first iteration or we've just finished another DNA
			if len(name) > 0 : # It's not the first iteration
				result.append(DNAstring)
				DNAstring = ''
			name = line.strip().replace('>', '')
		else :
			DNAstring += line.strip()
	if len(DNAstring) > 0 : # We've one unfinished entry
		result.append(DNAstring)
	return result[0], result[1:]

def translate(string, table):
	result = []
	for i in range(0, len(string), 3):
		result.append(str(table[string[i:i+3]]))
	result = ''.join(ch for ch in result)
	if result[-1:] == '*':
		return result[:-1]
	else:
		return result


def main():
	with open("Input.fasta", "r") as input_file:
		DNA, introns = read_DNAs_FASTA(input_file)
		prot = translate(remove_introns(DNA, introns), make_codons_table())
		print(prot)


main()
