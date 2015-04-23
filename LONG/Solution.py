#!/usr/bin/env python3

# Returns all DNAs as {name:string}
def read_DNAs_FASTA(input_file):
	result = {}
	name = ''
	DNAstring = ''
	for line in input_file:
		if '>' == line.strip()[0] : # Either it's the first iteration or we've just finished another DNA
			if len(name) > 0 : # It's not the first iteration
				result[name] = DNAstring
				DNAstring = ''
			name = line.strip().replace('>', '')
		else :
			DNAstring += line.strip()
	if len(DNAstring) > 0 : # We've one unfinished entry
		result[name] = DNAstring
	return result

def make_tiling_table(strings):
	length = len(strings)
	tiling_table = []
	def get_tiling_length(s1, s2):
		for offset in range(len(s1)):
			for j in range(min(len(s1) - offset, len(s2))):
				if s1[offset + j] != s2[j]:
					break
			else:
				return j
		else:
			return 0

	for i in range(length):
		tmp = []
#		tmp = {}
		for j in range(length):
			tmp.append(None if i == j else get_tiling_length(strings[i], strings[j]))
		tiling_table.append(tmp)
	return tiling_table

def get_shortest_superstring_recipe(tiling_table):
	def compose(head, pieces):
#		print("C:", head, pieces)
		score, recipe = 0, []
		if len(pieces) == 0:
			return 0, [head]
		pieces_weights = map(lambda p:(p, tiling_table[head][p-1]), pieces)# p-1 because of a trick in launching, see further
		pieces_weights = sorted(pieces_weights, key=lambda pw: pw[1])
		i = 0
		for piece, weight in pieces_weights:
			tmp_pieces = pieces[:]
			tmp_pieces.remove(piece)
			tmp_score, tmp_recipe = compose(piece, tmp_pieces)
			if tmp_score + weight > score:
				score = tmp_score + weight
				recipe = tmp_recipe
#!!!
			i += 1
			if i > 2:
				break
#!!!
		return score, [head] + recipe

	tiling_table.insert(0, [0 for i in range(len(tiling_table))]) # Eases launch
	score, recipe = compose(0, list(range(1, len(tiling_table))))
	del tiling_table[0]
	recipe.remove(0)
	return list(map(lambda x: x-1, recipe))

def construct_string(strings, tiling_table, recipe):
	string = '' + strings[recipe[0]]
	previous_piece = recipe[0]
	for piece in recipe[1:]:
		offset = tiling_table[previous_piece][piece]
		string += strings[piece][offset + 1:]
		previous_piece = piece
	return string

def main():
	with open("Input.fasta") as input_file:
		print("Reading input file...")
		strings = list(read_DNAs_FASTA(input_file).values())
		print("Making tiling_table...")
		tiling_table = make_tiling_table(strings)
		print(tiling_table)
#		return
		print("Getting recipe...")
		recipe = get_shortest_superstring_recipe(tiling_table)
		print(recipe)
		with open("Output.txt", "w") as output_file:
			print(construct_string(strings, tiling_table, recipe), file=output_file)

main()
