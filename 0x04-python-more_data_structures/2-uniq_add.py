#!/usr/bin/python3

def uniq_add(my_list=[]):
	num = set(my_list)
	total = 0
	for counter in num:
		total = total + counter
	return total
