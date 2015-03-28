#!/usr/bin/env python3

def read_correspondence_table(input_file, table):
	for line in input_file:
		table[line.strip()[0:3]] = line.strip()[4:8]

def translate_sliced_string(sliced_string, table):
	result = ''
	for piece in sliced_string:
		if table[piece] == "Stop":
			break
		else:
			result += table[piece]
	return result

def slice_by_3(string):
	result = []
	for i in range(int(len(string)/3)):
		result.append(string[3 * i:3 + 3 * i])
	return result

def translate_string(string, table):
	return translate_sliced_string(slice_by_3(string), table)

def main():
	with open("Codons_proteins_table.txt", "r") as table_file:
		codons_table = {}
		read_correspondence_table(table_file, codons_table)
		with open("Input.txt", "r") as input_file:
			with open("Output.txt", "w") as output_file:
				RNAstring = input_file.readline().strip()
				print(translate_string(RNAstring, codons_table), file=output_file)
main()
