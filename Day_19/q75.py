def transpose_matrix(mat: list[list[int]]) -> list[list[int]]:
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

if __name__ == "__main__":
    print("Example 2x3 transpose:")
    mat = [[1, 2, 3], [4, 5, 6]]
    print(transpose_matrix(mat))
