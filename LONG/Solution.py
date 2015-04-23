#!/usr/bin/env python3
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

def get_tiling_length(s1, s2):
	for offset in range(len(s1)):
		for j in range(min(len(s1) - offset, len(s2))):
			if s1[offset + j] != s2[j]:
				break
		else:
			return min(len(s1) - offset, len(s2))
	else:
		return 0

def overlap_cat(s1, s2):
	offset = get_tiling_length(s1,s2)
	return s1 + s2[offset:]


def sure_reduction(strings):
	number_of_strings = len(strings)

	def get_sure_things():
		sure_things = {}
		sure_length = len(strings[0]) // 2 # Heuristic that is said to work on our input
		for i in range(number_of_strings):
			for j in range(number_of_strings):
				if i == j:
					continue
				if get_tiling_length(strings[i], strings[j]) > sure_length:
					sure_things[i] = j

		return sure_things

	def get_contigs(sure_things):
		contigs = []
		tails = set(sure_things.values())
		contig_heads = set(range(number_of_strings)) - tails # A string is either a start of contig or a continuation of it
		for head in contig_heads:
			cur = head
			contig = [head]
			while cur in sure_things:
				contig.append(sure_things[cur])
				cur = sure_things[cur]
			contigs.append(contig)
		return contigs

	def contig_reduction(contigs):
		result = []
		for contig in contigs:
			result.append(reduce(overlap_cat, map(lambda i: strings[i], contig)))
		return result
	return contig_reduction(get_contigs(get_sure_things()))
# end of sure_reduction

def main():
	with open("Input.fasta") as input_file:
		strings = list(read_DNAs_FASTA(input_file).values())
		with open("Output.txt", "w") as output_file:
			print(sure_reduction(strings)[0], file=output_file)# there's actually just one big contig in input data

main()
