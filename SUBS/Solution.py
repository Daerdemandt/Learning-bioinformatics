#!/usr/bin/env python3

def is_contained_at(string, substring, start, offset):
	if offset == len(substring):
		return True
	if string[start + offset] == substring[offset] :
		return is_contained_at(string, substring, start, offset + 1)
	else:
		return False

def get_occurencies(string, substring):
	result = []
	for i in range(len(string) - len(substring)):
		if (is_contained_at(string, substring, i, 0)):
			result.append(i + 1)
	return result

def list_to_string(inlist):
	return ''.join(str(v) + ' ' for v in inlist)

def main():
	with open("Input.txt", "r") as input_file :
		string = input_file.readline().strip()
		substring = input_file.readline().strip()
		print(list_to_string(get_occurencies(string, substring)))

main()
