import numpy as np

import re


class MatrixProcessor:

    def __init__(self, n_rows, n_cols, matrix):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.matrix = matrix

    @classmethod
    def matrix_builder(cls):
        dim = input().strip()
        if not re.match(r"\A\d+\s*\d+$", dim):
            print("Invalid input!")
            return main()
        else:
            n_rows, n_cols = dim.split()
            n_rows = int(n_rows)
            n_cols = int(n_cols)
            matrix = [[int(el) for el in input().split()] for _ in range(n_rows)]
            for row in range(len(matrix)):
                try:
                    message = f"Invalid row length, row {row + 1}"
                    assert len(matrix[row]) == n_cols, message
                except AssertionError as err:
                    print(err)
                    return main()
            return cls(n_rows, n_cols, np.array(matrix))


def matrix_printer(result):
    for r in result:
        print(*r)


def add_matrices(m1, m2):
    if not all([m1.n_rows == m2.n_rows, m1.n_cols == m2.n_cols]):
        print("ERROR")
        return main()
    return np.add(m1, m2)


def multiply_by_constant(m, const):
    return m.matrix * const


def take_constant():
    try:
        cnstnt = int(input())
    except ValueError:
        print("provide constant for multiplying")
        return take_constant()
    return cnstnt


def main():
    matrix_a = MatrixProcessor.matrix_builder()
    c = take_constant()
    result = multiply_by_constant(matrix_a, c)
    matrix_printer(result)


if __name__ == '__main__':
    main()
