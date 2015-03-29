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

def calculate_profile_matrix(DNAs):
	return list(map(lambda x: list(map(x.count, "ACGT")), zip(*DNAs.values())))

def calculate_consensus_string(profile_matrix):
	return ''.join(map(lambda x: "ACGT"[x.index(max(x))], profile_matrix))

def print_profile_matrix(profile_matrix, output_file):
	for i in range(len("ACGT")):
		print("{}: {}".format("ACGT"[i], ''.join(str(profile_matrix[v][i])+' ' for v in range(len(profile_matrix)))), file=output_file)

def main():
	with open("Input.txt", "r") as input_file:
		DNAs = read_DNAs_FASTA(input_file)
		profile_matrix = calculate_profile_matrix(DNAs)
		consensus_string = calculate_consensus_string(profile_matrix)
		with open("Output.txt", "w") as output_file:
			print(consensus_string, file=output_file)
			print_profile_matrix(profile_matrix, output_file)
main()
