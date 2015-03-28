#!/usr/bin/env python

def gc_count(string):
	return (float(string.count('G')) + string.count('C') ) / len(string)

def read_signatures(input_file, signatures):
	name = ''
	DNAstring = ''
	for line in input_file:
		if '>' == line.strip()[0] : # Either it's the first iteration or we've just finished another DNA
			if len(name) > 0 : # It's not the first iteration
				signatures[name] = gc_count(DNAstring)
				DNAstring = ''
			name = line.strip().replace('>', '')
		else :
			DNAstring += line.strip()
	if len(DNAstring) > 0 : # We've one unfinished entry
		signatures[name] = gc_count(DNAstring)

def find_entry_with_highest_gc(signatures):
	return max(signatures, key=signatures.get)

def print_entry_gc_in_percent(name, signatures):
	print("%s\n%.4f" % (name, (signatures[name] * 100)))

def main():
	signatures = {}
	with open("Input.txt", "r") as input_file:
		read_signatures(input_file, signatures)
	entry_found = find_entry_with_highest_gc(signatures)
	print_entry_gc_in_percent(entry_found, signatures)

main()
