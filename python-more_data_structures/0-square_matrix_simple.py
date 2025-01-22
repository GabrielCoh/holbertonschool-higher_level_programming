#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for number in matrix:
        new_number = [x ** 2 for x in number]
        new_matrix.append(new_number)
    return new_matrix
