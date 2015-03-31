#!/usr/bin/env python3
import operator, re
from functools import reduce

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

def make_codons_table(): # by LudditeCyborg
	bases = ['T', 'C', 'A', 'G']
	codons = [a+b+c for a in bases for b in bases for c in bases]
	amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
	return dict(zip(codons, amino_acids))

def lookup_aminos_codons(codons_table, amino):
	a = amino
	if a.lower() == 'stop' or a.lower() == 'end':
		a = '*'
	if a.lower() == 'start':
		a = 'M'
	return list(map(lambda item: item[0], filter(lambda item: item[1] == a, codons_table.items())))

def make_inverted_codons_table():
	cod_tab = make_codons_table()
	return {amino:lookup_aminos_codons(cod_tab, amino) for amino in cod_tab.values()}

def find_codons_by_amino(string, amino):
	cod_tab = make_codons_table()
	codons = lookup_aminos_codons(cod_tab, amino)
	regex_pattern = ''.join("(" + codon + ")|" for codon in codons)[:-1]
	regex = re.compile(regex_pattern, 0)
	pos = 0
	while pos < len(string):
		match = regex.search(string, pos)
		if not match:
			break
		yield match.start()
		pos = match.start() + 1

def slice_by_3(string):
	for i in range(int(len(string)/3)):
		yield string[3 * i:3 + 3 * i]

def findpos(array, num):
	result = len(array)
	for i in range(len(array))[::-1]:
		if array[i] > num:
			result = i
	return result

def reverse_compliment(string):
	compl = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	return ''.join(compl[ch] for ch in string[::-1])

def get_ORFs_direct(string):
#TODO: find a way to use sorted list to speedup searching
	stop_codons_positions_mixed = list(find_codons_by_amino(string, "Stop"))
	cod_len = 3
	stop_codons_positions = {num:list(filter(lambda pos: pos % cod_len == num, stop_codons_positions_mixed)) for num in range(cod_len)}
	for start_pos in find_codons_by_amino(string, "Start"):
		stops = stop_codons_positions[start_pos % cod_len]
		stop_num = findpos(stops, start_pos)
		if (stop_num == len(stops)):
			continue
		yield (start_pos, stops[stop_num])

def get_protein(ORF, string):
	codons = slice_by_3(string[ORF[0]: ORF[1] + 3])
	cod_tab = make_codons_table()
	return ''.join(cod_tab[cod] for cod in codons)[:-1]

def get_proteins_direct(string):
	return set(map(lambda x : get_protein(x, string), get_ORFs_direct(string)))

def get_proteins(string):
	proteins_direct = get_proteins_direct(string)
	proteins_revc = get_proteins_direct(reverse_compliment(string))
	return proteins_direct | proteins_revc

def main():
	with open("Input.fasta", "r") as input_file:
		string = list(read_DNAs_FASTA(input_file).values())[0]
		string = reverse_compliment(string)
		with open("Output.txt", "w") as output_file:
			for protein in get_proteins(string):
				print(protein, file=output_file)		

		
main()

