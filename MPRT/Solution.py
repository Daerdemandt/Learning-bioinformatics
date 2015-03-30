#!/usr/bin/env python3
#from urllib import urlretrieve
import urllib.request, os, os.path, re

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

def uniprot_get_fasta(uniprot_id):
	filename = uniprot_id + ".fasta"
	if not os.path.exists(filename):
		adress = "http://www.uniprot.org/uniprot/" + filename
		urllib.request.urlretrieve(adress, filename)
	fasta_file = open(filename, "r")
	string = list(read_DNAs_FASTA(fasta_file).values())[0]
	os.remove(filename)
	return (uniprot_id, string)

def search_motif_in_string(motif, string):
	regex = motif_to_regex(motif)
	pos = 0
	while pos < len(string):
		match = regex.search(string, pos)
		if not match:
			break
		yield match
		pos = match.start() + 1

def positions_to_string(matches):
	return ''.join(str(m.start()+1)+' ' for m in matches)

def motif_to_regex(string):
	return re.compile(string.replace("{", "[^").replace("}", "]"), 0)

def main():
	motif = "N{P}[ST]{P}"
	with open("Input.txt", "r") as input_file:
		uniprot_IDs = list(map(str.strip, input_file))
		for uniprot_id in uniprot_IDs:
			string = uniprot_get_fasta(uniprot_id)[1]
			pos_string = positions_to_string(search_motif_in_string(motif, string))
			if 0 < len(pos_string):
				print(uniprot_id)
				print(pos_string)

main()
