#!/usr/bin/env python3
from functools import reduce

def get_sums_distribution(dist1, dist2):
	max1 = max(list(dist1.keys()))
	max2 = max(list(dist2.keys()))
	result = {num:0 for num in range(max1 + max2 + 1)}
	for i in range(max1 + 1):
		for j in range(max2 + 1):
			result[i+j] += dist1[i] * dist2[j]
	return result

def get_selfsum_distribution(dist):
	return get_sums_distribution(dist, dist)

def get_powers2_distribution(max_power):
	if (0 == max_power):
		return [{0:0.75, 1:0.25}]
	result = get_powers2_distribution(max_power - 1)
	new_member = get_selfsum_distribution(result[max_power - 1])
	result.append(new_member)
	return result

def reversed_binary(number):
	return list(map(int, reversed((bin(number)[2:]))))

def get_numbers_distribution(number):
	pows_distr = get_powers2_distribution(number.bit_length())
	number_as_distributions = map(lambda x,y: x if 1 == y else {0:1}, pows_distr, reversed_binary(number))
	return reduce(get_sums_distribution, number_as_distributions)

def get_chance_of_at_least_N_in_m(N, m):
	dist = get_numbers_distribution(m)
	return sum(map(lambda x: x[1], filter(lambda x: x[0] >= N, dist.items())))

def main():
	k, N = 2, 1
	print(get_chance_of_at_least_N_in_m(N, pow(2, k)))

main()
