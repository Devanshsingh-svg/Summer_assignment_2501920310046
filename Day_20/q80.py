def column_wise_sum(mat: list[list[int]]) -> list[int]:
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]

if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Column-wise sum: {column_wise_sum(mat)}")
