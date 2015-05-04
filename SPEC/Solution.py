#!/usr/bin/env python3
from bisect import bisect

def get_amino_masses():
	with open("Amino_masses.txt") as input_file:
		def divide_line(line):
			(amino, mass) = line.strip().split()
			return amino, float(mass)
		return dict(divide_line(line) for line in input_file)

def differences(nums):
	return [abs(x[0] - x[1]) for x in zip(nums, nums[1:])]

def make_amino_finder(amino_dict):
	reverse_items = list({amino_dict[a]:a for a in amino_dict}.items())
	reverse_items.sort(key=lambda item: item[0])
	masses = [item[0] for item in reverse_items]
	aminos = [item[1] for item in reverse_items]
	assert len(aminos) > 0
	error_treshold = min(differences(masses)) / 2

	def get_amino(mass):
		index = bisect(masses, mass)
		def unfitness(index):
			return abs(masses[index] - mass)
		if index == len(aminos): # given mass is too big
			index -= 1
		if 	index != 0:
			if unfitness(index) > unfitness(index - 1):
				index = index - 1
		assert unfitness(index) < error_treshold
		return aminos[index]
	return get_amino


def main():
	with open("Input.txt") as input_file:
		masses = [float(line.strip()) for line in input_file]
		masses.sort()
		amino_finder = make_amino_finder(get_amino_masses())
		aminos = [amino_finder(mass) for mass in differences(masses)]
		print(''.join(aminos))

main()
