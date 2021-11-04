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
            return cls(n_rows, n_cols, matrix)


def main():
    a = MatrixProcessor.matrix_builder()
    b = MatrixProcessor.matrix_builder()

    if not all([a.n_rows == b.n_rows, a.n_cols == b.n_cols]):
        print("ERROR")
    else:
        print()
        result = np.add(a.matrix, b.matrix)

        for r in result:
            print(*r)


if __name__ == '__main__':
    main()
