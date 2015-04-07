#!/usr/bin/env python3

def get_strings(alphabet, length):
	if length == 0:
		yield ''
	else:
		for ch in alphabet:
			for st in get_strings(alphabet, length - 1):
				yield ch + st

def main():
	alphabet = "T A G C".split()
	length = 2
	with open("Output.txt", "w") as output_file:
		for st in get_strings(alphabet, length):
			print(st, file=output_file)


main()
