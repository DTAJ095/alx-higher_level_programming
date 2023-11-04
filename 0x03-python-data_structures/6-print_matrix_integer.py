#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        len_m = 1
        for j in i:
            if len_m == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end="")
            len_m += 1
        print()
