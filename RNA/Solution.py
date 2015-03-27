#!/usr/bin/env python

# Translating DNA to RNA by replacing each 'T' with 'U'

with open("Input.txt", "r") as input_file:
	print(input_file.readline().strip().replace('T', 'U'))
