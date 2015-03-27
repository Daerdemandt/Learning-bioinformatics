#!/usr/bin/env python
n, m = 6, 3

main_list = [1]

def iterate_list(x):
	# Breeding, aging
	if len(x) == 1 :
		x.insert(0, 0)
	else :
		x.insert(0, sum(x[1::]))
	# Dying of old age
	if len(x) > m :
		del x[m]

for i in range(1, n) :
	iterate_list(main_list)

print(sum(main_list))
