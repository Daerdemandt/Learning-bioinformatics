#!/usr/bin/env python3
from math import log10

def get_string_prob(string, gc):
	gc_count = string.count('G') + string.count('C')
	if gc == 0:
		if gc_count == 0:
			return 0.5 ** len(string)
		else:
			return 0
	if gc == 1:
		if gc_count == len(string):
			return 0.5 ** len(string)
		else:
			return 0
	gc_log, at_log = log10(gc/2), log10((1 - gc)/2)
	return 10 ** (gc_count * gc_log + (len(string) - gc_count) * at_log)

def number_of_attempts(N, string):
	return N + 1 - len(string)

def expected_occurencies(N, string, gc):
	return get_string_prob(string, gc) * number_of_attempts(N, string)

def print_float_list(float_list):
	print(''.join('{:5.3f} '.format(fl) for fl in float_list))

def main():
	with open("Input.txt", "r") as input_file:
		N = int(input_file.readline().strip())
		string = input_file.readline().strip()
		gcs = [float(gc) for gc in input_file.readline().strip().split()]
		print_float_list(expected_occurencies(N, string, gc) for gc in gcs)


main()
