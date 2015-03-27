#!/usr/bin/env python

def translate(x):
	return {'A':'T', 'T':'A', 'C':'G', 'G':'C'}[x]

with open("Input.txt", "r") as input_file:
		inversed_string = input_file.readline().strip()[::-1]
		print(''.join(map(translate, inversed_string)))
