def multiply_matrices(mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
    res = [[0] * len(mat2[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[2, 0], [1, 2]]
    print("Multiplication result:")
    print(multiply_matrices(mat1, mat2))
