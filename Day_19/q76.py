def diagonal_sum(mat: list[list[int]]) -> int:
    n = len(mat)
    return sum(mat[i][i] + mat[i][n - 1 - i] for i in range(n)) - (mat[n//2][n//2] if n % 2 != 0 else 0)

if __name__ == "__main__":
    print("Example 3x3 diagonal sum:")
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(diagonal_sum(mat))
