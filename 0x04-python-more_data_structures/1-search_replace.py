#!/usr/bin/python3

def search_replace(my_list, search, replace):
	new_list = []
	for counter in my_list:
		if counter == search:
			new_list.append(replace)
		else :
				new_list.append(counter)
	return new_list
