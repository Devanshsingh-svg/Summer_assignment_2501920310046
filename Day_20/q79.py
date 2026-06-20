def row_wise_sum(mat: list[list[int]]) -> list[int]:
    return [sum(row) for row in mat]

if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Row-wise sum: {row_wise_sum(mat)}")
