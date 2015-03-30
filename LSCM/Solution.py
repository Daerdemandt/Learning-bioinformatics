#!/usr/bin/env python3

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

def is_contained_in(sub, string):
	return (-1 != string.find(sub))

def get_common_substring(strings, base_string, length):
	if length > len(base_string):
		return ""
	for i in range(1 + len(base_string) - length):
		sub = base_string[i:i+length]
		contained_count = 0
		for string in strings:
			if is_contained_in(sub, string):
				contained_count += 1
			else:
				break
		if contained_count == len(strings):
			return sub
	return ""

def get_shortest_string(strings):
	lengths = list(map(lambda x: len(x), strings))
	shortest_index = lengths.index(min(lengths))
	return(strings[shortest_index])

def get_longest_common_substring(strings):
	shortest_string = get_shortest_string(strings)
	for length in range(len(shortest_string), 0, -1):
		sub = get_common_substring(strings, shortest_string, length)
		if len(sub) > 0:
			return sub
	return ""


def main():
	with open("Input.txt", "r") as input_file:
		with open("Output.txt", "w") as output_file:
			strings = list(read_DNAs_FASTA(input_file).values())
			print(get_longest_common_substring(strings), file=output_file)
		
main()
