def subtract_matrices(mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
    return [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

if __name__ == "__main__":
    print("Example 2x2 subtraction:")
    mat1 = [[5, 6], [7, 8]]
    mat2 = [[1, 2], [3, 4]]
    print(subtract_matrices(mat1, mat2))
