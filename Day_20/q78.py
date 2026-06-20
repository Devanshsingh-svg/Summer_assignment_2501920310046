def check_symmetric(mat: list[list[int]]) -> bool:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != mat[j][i]: return False
    return True

if __name__ == "__main__":
    mat = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
    print(f"Matrix is symmetric: {check_symmetric(mat)}")
