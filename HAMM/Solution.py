#!/usr/bin/env python3

def read_2_strings(input_file):
	return input_file.readline().strip(), input_file.readline().strip()

def count_hamming(strtuple):
	diffs = 0
	for ch1, ch2 in zip(strtuple[0], strtuple[1]):
		if ch1 != ch2:
			diffs += 1
	return diffs

def main():
	with open("Input.txt", "r") as input_file:
		print(count_hamming(read_2_strings(input_file)))

main()
