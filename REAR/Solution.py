#!/usr/bin/env python3

def get_permutation(pair):
	s1, s2 = pair[0], pair[1]
	assert len(s1) == len(s2)
	def inv(seq):
		return list(map(lambda x: seq.index(x) + 1, range(1, 1 + len(seq))))
	def mul(seq1, seq2):
		return list(map(lambda x: seq1[x-1], seq2))
	return mul(inv(s2), s1)

def read_perms(input_file):
	seqs = []
	for line in input_file.readlines():
		if len(line.strip()) > 0:
			seqs.append(list(map(int, line.strip().split())))
		if len(seqs) == 2:
			yield get_permutation(seqs)
			seqs = []

def segmentise_perm(perm):
	result = []
	capacitor = []
	def monotonous_further(i):
		return i + 1 < len(perm) and abs(perm[i + 1] - perm[i]) == 1

	for i in range(len(perm)):
		if len(capacitor) > 0:
			capacitor.append(perm[i])
			if not monotonous_further(i):# we can't switch from ascending to descending and keep diff == 1 because elements are unique
				result.append(capacitor)
				capacitor = []
		else:
			if monotonous_further(i):
				capacitor.append(perm[i])
			else:
				result.append([perm[i]])
	return result

def get_flips(segmentised_permutation):
	perm = segmentised_permutation
	good = []
	better = []
	length = len(segmentised_permutation)
	def merges(seq1, seq2): # assumes uniqueness of elements
		return abs(seq1[-1] - seq2[0]) == 1
	def get_score(i,j):
		start_merges = j + 1 != length and merges(perm[i][::-1], perm[j + 1])
		end_merges = i != 0 and merges(perm[i - 1], perm[j][::-1])
		return start_merges + end_merges
	for i in range(length):
		for j in range(i, length):
			score = get_score(i,j)
			if 1 == score:
				good.append((i,j))
			if 2 == score:
				better.append((i,j))
	return good, better

# Getting reversal distance is NP-complete task. There are solutions that work faster than this, but they're more complicated.
# This solution uses 3 assumptions - we don't split monotonous sectors, all elements are unique and each step reduces number of monotonous sectors.
def get_reversal_distance(segmentised_permutation):
	if len(segmentised_permutation) == 1:
		if segmentised_permutation[0][0] == 1:#correct order
			return 0
		else: #monotonous sequence. Incorrect order. 1 more flip needed
			return 1 
	flips = get_flips(segmentised_permutation)
	good_flips = flips[0]
	better_flips = flips[1]
	result = len(segmentised_permutation)
	def get_flipped(perm, flip):
		i, j = flip[0], flip[1]
		result = perm[:] # copy
		result[i:j + 1] = list(map(lambda x: x[::-1], perm[i:j + 1][::-1])) # flip
		if j + 1 < len(result) and abs(result[j][-1] - result[j+1][0]) == 1: # merge if needed. Assuming elements are unique.
			result[j] = result[j] + result[j+1]
			del result[j+1]
		if i > 0 and abs(result[i][0] - result[i-1][-1]) == 1: #same here
			result[i-1] = result[i-1] + result[i]
			del result[i]
		return result

	for flip in better_flips + good_flips:
		score = get_reversal_distance(get_flipped(segmentised_permutation, flip))
		if score + 1 < result:
			result = score + 1
	return result

def main():
	with open("Input.txt") as input_file:
		print(''.join(str(x) + ' ' for x in map(get_reversal_distance, map(segmentise_perm, read_perms(input_file)))))


main()
