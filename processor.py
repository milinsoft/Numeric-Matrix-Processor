import numpy as np

import re


def matrix_builder(dim_message=None, matrix_message=None) -> dict(description="matrix", type=np.ndarray):
    dim = input(dim_message).strip()
    if not re.match(r"\A\d+\s*\d+$", dim):
        print("Invalid input!")
        return main()
    else:
        n_rows, n_cols = [int(x) for x in dim.split()]
        print(matrix_message)
        matrix = [[float(el) for el in input().split()]for _ in range(n_rows)]
        """ shape validation """
        for row in range(len(matrix)):
            try:
                message = f"Invalid row length, row {row + 1}"
                assert len(matrix[row]) == n_cols, message
            except AssertionError as err:
                print(err)
                return main()

        return np.array(matrix)


def matrix_printer(result):
    print("The result is:")
    for r in result:
        print(*r)


def add_matrices(m1: np.ndarray, m2: np.ndarray) -> dict(description="matrix", type=np.ndarray):
    if not all([m1.shape[0] == m2.shape[0],
                m1.shape[1] == m2.shape[1]]):
        print("ERROR")
        return main()
    return np.add(m1, m2)


def multiply_by_constant(matrix: np.ndarray, const) -> dict(description="matrix", type=np.ndarray):
    return matrix * const


def take_constant() -> int:
    try:
        cnstnt = int(input())
    except ValueError:
        print("provide constant for multiplying")
        return take_constant()
    return cnstnt


def multiply_matrices(m1: np.ndarray, m2: np.ndarray) -> dict(description="matrix", type=np.ndarray):
    try:
        result = np.matmul(m1, m2)  # https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
    except ValueError:
        print("ERROR")
        return main()
    return result


def main():
    """ main menu"""
    while True:
        option = input("1. Add matrices\n2. Multiply matrix by a constant\n3. Multipl matrices\n4. Transpose matrix\n5. Calculate a determinant\nInverse matrix\n0. Exit\nYour choice: ")
        if option == "0":
            exit()

        elif option in {"1", "3"}:
            """ Add two matrices / Multiply two matrices"""
            matrix_a = matrix_builder("Enter size of first matrix: ", "Enter first matrix:")
            matrix_b = matrix_builder("Enter size of second matrix: ", "Enter second matrix:")
            result = add_matrices(matrix_a, matrix_b) if option == "1" else multiply_matrices(matrix_a, matrix_b)
            matrix_printer(result)

        elif option == "2":
            """ Multiply matrix by a constant """
            matrix_a = matrix_builder("Enter size of matrix: ", "Enter matrix:")
            constant = take_constant()
            result = multiply_by_constant(matrix_a, constant)
            matrix_printer(result)

        elif option == "4":
            """ Transpose matrix """
            transposition_type = input("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line\nYour choice: ")
            matrix_a = matrix_builder("Enter size of matrix: ", "Enter matrix:")

            transpositions = {"1": matrix_a.transpose(),  # standard main diagonal transposion
                              "2":  np.fliplr(np.rot90(matrix_a, 1)),  # side diagonal transposion is done throug one 90 degree counterclock-wise rotation and horizontal - line flip (simply row = row [::-1].
                              "3": np.flip(matrix_a, 1),  # reversing order of elements along the given axis
                              "4": np.flipud(matrix_a),  # vertical flip, replacing the sequence of rows moving the top ones to the bottom. Similar to stack operations
                              }  # can be stored as tuple to save some memory

            try:
                matrix_printer(transpositions[transposition_type])
            except KeyError:
                print("Invalid option chosen.")
                return main()

        elif option == "5":
            matrix_a = matrix_builder("Enter size of matrix: ", "Enter matrix:")
            result = np.linalg.det(matrix_a)
            print(result)

        elif option == "6":
            matrix_a = matrix_builder("Enter size of matrix: ", "Enter matrix:")
            det = np.linalg.det(matrix_a)
            if det == 0:
                print("This matrix doesn't have an inverse.")
            else:
                result = np.linalg.inv(matrix_a)
                matrix_printer(result)

        else:
            print("Invalid option chosen.")
            return main()


if __name__ == '__main__':
    main()
