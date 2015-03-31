#!/usr/bin/env python3

def get_amino_masses(input_file):
	return dict(line.strip().split() for line in input_file)

def get_string_mass(string, masses_dict):
	return sum(map(lambda ch: float(masses_dict[ch]), string))

def main():
	with open("Amino_masses.txt", "r") as input_file:
		mass_dict = get_amino_masses(input_file)
		string = "SKADYEK"
		print(get_string_mass(string, mass_dict))
main()
