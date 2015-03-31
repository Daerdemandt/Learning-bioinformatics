#!/usr/bin/env python3
from math import factorial
from functools import reduce

def get_placements_by_number(number, number_of_elements):
	num = number
	for base in range(number_of_elements, 0, -1):
		yield(num % base)
		num = num // base

def get_permutation_by_placements(placements):
	result = []
	number_to_place = 0
	for place in reversed(list(placements)):
		result.insert(place, number_to_place)
		number_to_place += 1
	return result

def get_permutation_by_number(number, number_of_elements):
	return get_permutation_by_placements(get_placements_by_number(number, number_of_elements))

def get_placements_by_permutation(permutation):
	perm = permutation[:]
	number_to_place = max(permutation)
	while number_to_place >= 0:
		res = perm.index(number_to_place)
		del(perm[res])
		number_to_place -= 1
		yield res

def get_number_by_placements(placements):
	p_rev = list(reversed(list(placements)))
	highest_element = len(p_rev) - 1
	placed_elements = range(highest_element + 1)
	num = 0
	for elem in placed_elements:
		num *= elem + 1
		num += p_rev[elem]
	return num

def get_number_by_permutation(permutation):
	return get_number_by_placements(get_placements_by_permutation(permutation))

def print_permutation(perm, output_file):
	print(''.join(str(v + 1) + ' ' for v in perm), file=output_file)

def main():
	the_number = 3
	with open("Output.txt", "w") as output_file:
		print(factorial(the_number), file=output_file)
		for i in range(factorial(the_number)):
			print_permutation(get_permutation_by_number(i, the_number), output_file)

main()
