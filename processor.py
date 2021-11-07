import numpy as np

import re


def matrix_builder(dim_message=None, matrix_message=None):
    dim = input(dim_message).strip()
    if not re.match(r"\A\d+\s*\d+$", dim):
        print("Invalid input!")
        return main()
    else:
        n_rows, n_cols = [int(x) for x in dim.split()]
        print(matrix_message)
        matrix = np.array([[float(el) for el in input().split()]for _ in range(n_rows)])
        for row in range(len(matrix)):
            try:
                message = f"Invalid row length, row {row + 1}"
                assert len(matrix[row]) == matrix.shape[1], message
            except AssertionError as err:
                print(err)
                return main()
        return matrix


def matrix_printer(result):
    print("The result is:")
    for r in result:
        print(*r)


def add_matrices(m1, m2):
    if not all([m1.shape[0] == m2.shape[0], m1.shape[1] == m2.shape[1]]):
        print("ERROR")
        return main()
    return np.add(m1, m2)


def multiply_by_constant(matrix, const):
    return matrix * const


def take_constant():
    try:
        cnstnt = int(input())
    except ValueError:
        print("provide constant for multiplying")
        return take_constant()
    return cnstnt


def multiply_matrices(m1, m2):
    if m1.shape[1] != m2.shape[0]:
        print("ERROR")
        return main()
    # return np.multiply(m1, m2)
    return np.matmul(m1, m2)  # https://numpy.org/doc/stable/reference/generated/numpy.matmul.html


def main():
    """ main menu"""
    while True:
        try:
            option = int(input("1. Add matrices\n2. Multiply matrix by a constant\n3. Multipl matrices\n0. Exit\nYour choice: "))
        except ValueError:
            print("PICK THE OPTION FROM THE LIST!")
            return main()
        if option == 0:
            exit()
        elif option == 1:
            """ Add two matrices """
            matrix_a = matrix_builder("Enter size of first matrix: ", "Enter first matrix:")
            matrix_b = matrix_builder("Enter size of second matrix: ", "Enter second matrix:")
            result = add_matrices(matrix_a, matrix_b)
            matrix_printer(result)
        elif option == 2:
            """ Multiply matrix by a constant """
            matrix_a = matrix_builder("Enter size of matrix: ", "Enter matrix:")
            constant = take_constant()
            result = multiply_by_constant(matrix_a, constant)
            matrix_printer(result)

        elif option == 3:
            " Multiply two matrices "
            print("not yet implemented")
            matrix_a = matrix_builder("Enter size of first matrix: ", "Enter first matrix:")
            matrix_b = matrix_builder("Enter size of second matrix: ", "Enter second matrix:")
            result = multiply_matrices(matrix_a, matrix_b)
            matrix_printer(result)


if __name__ == '__main__':
    main()
