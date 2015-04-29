#!/usr/bin/env python3

def get_permutation(pair):
	s1, s2 = pair[0], pair[1]
	assert len(s1) == len(s2)
	def inv(seq):
		return list(map(lambda x: seq.index(x) + 1, range(1, 1 + len(seq))))
	def mul(seq1, seq2):
		return list(map(lambda x: seq1[x-1], seq2))
	return mul(inv(s1), s2)

def read_perms(input_file):
	seqs = []
	for line in input_file.readlines():
		if len(line.strip()) > 0:
			seqs.append(list(map(int, line.strip().split())))
		if len(seqs) == 2:
			yield get_permutation(seqs)
			seqs = []

# Get list of reversals that transform identity permutation into given permutation. Permutation is given as a list of numbers with the lowest number being 1. Reversals are 0-based
def get_reversals(permutation):
# Declaring functions:
	# Transform permutation into segmentised permutation: list of segments, in each segment neighbouring element differ exactly by 1
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

	def unsegmentise_reversal(segmentised_reversal, segmentised_perm):
		first_segm, last_segm = segmentised_reversal[0], segmentised_reversal[1]
		assert first_segm <= last_segm
		assert last_segm < len(segmentised_perm)
		first_symbol_number = sum(map(len, segmentised_perm[:first_segm]))
		last_symbol_number = sum(map(len, segmentised_perm[:last_segm + 1])) - 1
		return (first_symbol_number, last_symbol_number) # 0-indexed

	# Transforming permutation into identity permutation
	# Getting reversal distance is NP-complete task. There are solutions that work faster than this, but they're more complicated.
	# This solution uses 3 assumptions - we don't split monotonous sectors, all elements are unique and each step reduces number of monotonous sectors.
	def get_reversals_segmentised(segmentised_permutation):
		if len(segmentised_permutation) == 1:
			if segmentised_permutation[0][0] == 1:#correct order
				return []
			else: #monotonous sequence. Incorrect order. 1 more flip needed - to reverse the only remaining segment
				return [(0, 0)]
		flips = get_flips(segmentised_permutation)

		result = [(0,0) for i in range(2 * len(segmentised_permutation))] # bad result, will be returned only if there're absolutely no flips
		score = len(segmentised_permutation)
		for flip in flips:
			tmp = get_reversals_segmentised(get_flipped_segm_perm(segmentised_permutation, flip))
			if len(tmp) + 1 < score:
				result = [flip] + tmp
				score = len(result)
		return result

	# Get list of reversals that reduce number of segments by causing merges
	def get_flips(segmentised_permutation):
		perm = segmentised_permutation
		good, better = [], []
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
				if 0 == score:
					continue
				(good if score == 1 else better).append((i,j))
		return better + good # So first there're all better variants
			

	def get_flipped_segm_perm(segm_perm, flip):
		i, j = flip[0], flip[1]
		result = segm_perm[:] # copy
		result[i:j + 1] = list(map(lambda x: x[::-1], segm_perm[i:j + 1][::-1])) # flip
		if j + 1 < len(result) and abs(result[j][-1] - result[j+1][0]) == 1: # merge if needed. Assuming elements are unique.
			result[j] = result[j] + result[j+1]
			del result[j+1]
		if i > 0 and abs(result[i][0] - result[i-1][-1]) == 1: #same here
			result[i-1] = result[i-1] + result[i]
			del result[i]
		return result

# End of declaring functions
	segm_perm = segmentise_perm(permutation)
	segm_reversals = get_reversals_segmentised(segm_perm)
	reversals = []
	for segm_rev in segm_reversals:
		reversal = unsegmentise_reversal(segm_rev, segm_perm)
		reversals = [reversal] + reversals
		segm_perm = get_flipped_segm_perm(segm_perm, segm_rev)
	assert len(segm_perm) == 1
	return reversals
# end of get_reversals

def print_reversals(reversals):
	print(len(reversals))
	for rev in reversals:
		print(rev[0] + 1, rev[1] + 1) # 0-indexed to 1-indexed

def main():
	with open("Input.txt") as input_file:
		perms = list(read_perms(input_file))
		print_reversals(get_reversals(perms[0]))


main()
