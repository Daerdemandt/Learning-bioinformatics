#!/usr/bin/env python3
from math import log10

def get_string_probability_lg(string, gc):
	gc_count = string.count('G') + string.count('C')
	gc_log, at_log = log10(gc/2), log10((1 - gc)/2)
	return gc_count * gc_log + (len(string) - gc_count) * at_log
	

def main():
	with open("Input.txt", "r") as input_file:
		string = input_file.readline().strip()
		gc_counts = [float(num) for num in input_file.readline().strip().split()]
		print(''.join('{:5.3f} '.format(lgsum) for lgsum in map(lambda x : get_string_probability_lg(string, x), gc_counts)))


main()
