#!/usr/bin/env python3

genotypes = ["DD", "DR", "RR"]
childs_per_couple = 2

input_string = "1 0 0 1 0 1"

def recessive_heritage_chance(parent_genotype) :
	return float(parent_genotype.count('R')) / len(parent_genotype)

def recessive_genotype_chance(genotype1, genotype2) :
	return recessive_heritage_chance(genotype1) * recessive_heritage_chance(genotype2)

def dominant_genotype_chance(genotype1, genotype2) :
	return 1 - recessive_genotype_chance(genotype1, genotype2)

def make_chances_table(genotypes) :
	result = []
	for parent1 in genotypes :
		for parent2 in genotypes[genotypes.index(parent1):] :
			result.append(dominant_genotype_chance(parent1, parent2))
	return result

def parse_couples_numbers(input_string):
	return list(map(int, input_string.split()))

def estimate_dominant_offspring(input_string):
	return sum(map(lambda chan, num: chan * num * childs_per_couple, make_chances_table(genotypes), parse_couples_numbers(input_string)))


def main():
	print(estimate_dominant_offspring(input_string))
main()
