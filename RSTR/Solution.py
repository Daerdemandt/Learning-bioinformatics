#!/usr/bin/env python3
from math import log10

def get_string_prob(string, gc):
	gc_count = string.count('G') + string.count('C')
	gc_log, at_log = log10(gc/2), log10((1 - gc)/2)
	return 10 ** (gc_count * gc_log + (len(string) - gc_count) * at_log)

def at_least_1_success_prob(N, success_prob):
	fail_prob = 1- success_prob
	N_fails_prob = fail_prob ** N
	return 1 - N_fails_prob
	

def main():
	with open("Input.txt", "r") as input_file:
		(N, gc) = input_file.readline().strip().split()
		N, gc = int(N), float(gc)
		string = input_file.readline().strip()
		probability = get_string_prob(string, gc)
		print('{:5.3f}'.format(at_least_1_success_prob(N, probability)))


main()
