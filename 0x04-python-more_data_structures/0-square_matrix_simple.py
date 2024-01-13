#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
	new_matrix = []
	for num in matrix:
		square = list(map(lambda x : x ** 2, num))
		new_matrix.append(square)
	return new_matrix
