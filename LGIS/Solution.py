#!/usr/bin/env python3

def longest_increasing_subsequence(seq):
# It may be optimised not to store the whole pretendent bodies
	pretendent_tails_indexes = [''] # [i] is the least possible tail of sub of len i
	pretendent_bodies = [[]] # [i] is the body of pretendent of len i
	def upgrade_pretendent(length, element):
		if len(pretendent_tails_indexes) <= length + 1:
			pretendent_tails_indexes.append(0)
			pretendent_bodies.append(0)
		pretendent_tails_indexes[length + 1] = element
		pretendent_bodies[length + 1] = list(pretendent_bodies[length])
		pretendent_bodies[length + 1].append(seq[element])

	def find_element_to_upgrade_with(element): # Finds largest i that seq[pti[i]] < elem
		for i in range(1, len(pretendent_tails_indexes),)[::-1]:
			if seq[pretendent_tails_indexes[i]] < element:
				return i
		return 0

	pretendent_tails_indexes.append(0)
	pretendent_bodies.append([seq[0]])
	for i in range(1, len(seq)):
		index = find_element_to_upgrade_with(seq[i])
		upgrade_pretendent(index, i)
	return pretendent_bodies[-1]
# end of longest_increasing_subsequence

def read_sequence(input_file):
	n = int(input_file.readline().strip())
	seq = list(map(int, input_file.readline().strip().split()))
	assert len(seq) == n
	return seq

def print_seq(seq, output_file):
	print(''.join(str(elem) + ' ' for elem in seq), file=output_file)

def invapply(func, seq):
	n = len(seq)
	def inv(seq):
		return map(lambda x: n - x, seq)
	return list(inv(func(list(inv(seq)))))

def main():
	with open("Input.txt", "r") as input_file:
		seq = read_sequence(input_file)
		with open("Output.txt", "w") as output_file:
			print_seq(longest_increasing_subsequence(seq), output_file)
			print_seq(invapply(longest_increasing_subsequence, seq), output_file)

main()
