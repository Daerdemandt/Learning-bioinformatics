#!/usr/bin/env python3

# Input numbers
# Given to be positive integers
k, m, n = 2, 2, 2
gene_pool = {"DD":k, "DR":m, "RR":n}

def recessive_heritage_chance(parent_genotype) :
	return float(parent_genotype.count('R')) / len(parent_genotype)

def recessive_genotype_chance(genotype1, genotype2) :
	return recessive_heritage_chance(genotype1) * recessive_heritage_chance(genotype2)

def dominant_genotype_chance(genotype1, genotype2) :
	return 1 - recessive_genotype_chance(genotype1, genotype2)

# TODO: find a way to name fields, i.e. 'variants[genotype].chance'
def get_variants(gene_pool):
	population_size = sum(gene_pool.values())
	variants = {}
	for genotype in gene_pool.keys(): 
		if 0 != gene_pool[genotype] :
			reduced_pool = gene_pool.copy()
			reduced_pool[genotype] -= 1
			chance = float(gene_pool[genotype]) / population_size
			variants[genotype] = (chance, reduced_pool)
	return variants

def count_total_dominant_chance():
	dominant_chance = 0.0
	variants = get_variants(gene_pool)
	for genotype1 in variants.keys():
		mate_variants = get_variants(variants[genotype1][1])
		for genotype2 in mate_variants.keys():
			mate_chance = mate_variants[genotype2][0] * variants[genotype1][0]
			dominant_chance += mate_chance * dominant_genotype_chance(genotype1, genotype2)
	return dominant_chance

def main():
	print(count_total_dominant_chance())

main()
