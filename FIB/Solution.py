#!/usr/bin/env python
n,k = 5, 3

def number(month):
	if 1 == month or 2 == month:
		return 1
	else:
		return number(month - 1) + k * number(month - 2)

print(number(n))
