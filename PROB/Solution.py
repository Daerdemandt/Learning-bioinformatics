#!/usr/bin/env python3
from math import log10

def get_string_probability_lg(string, gc_count):
	char_prob = {'A' : (1 - gc_count) / 2, 'T' : (1 - gc_count) / 2, 'C' : gc_count / 2, 'G' : gc_count / 2}
	exact_prob_lgs = [log10(char_prob[char]) for char in string]
	return sum(exact_prob_lgs)
	

def main():
	with open("Input.txt", "r") as input_file:
		string = input_file.readline().strip()
		gc_counts = [float(num) for num in input_file.readline().strip().split()]
		print(''.join('{:5.3f} '.format(lgsum) for lgsum in map(lambda x : get_string_probability_lg(string, x), gc_counts)))


main()
