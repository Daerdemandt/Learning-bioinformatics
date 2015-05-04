#!/usr/bin/env python3

def read_fasta_string(input_file):
	multistring = input_file.readlines()[1:]
	return ''.join(string.strip() for string in multistring)

def failure_array(string):
	pretendents = [] # indexes of starting position of "string"
	yield 0
	def fails(pretendent, index):
		assert pretendent <= index
		return string[index] != string[index - pretendent]
	for index in range(1, len(string)):
		pretendents.append(index)
		pretendents = [p for p in pretendents if not fails(p, index)]
		yield (index - min(pretendents) + 1) if pretendents else 0

def print_list_int(int_list, output_file):
	print(' '.join(str(i) for i in int_list), file=output_file)

def main():
	with open("Input.fasta") as input_file:
		with open("Output.txt", "w") as output_file:
			print_list_int(failure_array(read_fasta_string(input_file)), output_file)

main()
