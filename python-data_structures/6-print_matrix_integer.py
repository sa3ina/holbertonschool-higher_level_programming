#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in range(len(row)):
            if elem != 0:
                print(" ", end="")
            print("{:d}".format(row[elem]), end="")
        print()
