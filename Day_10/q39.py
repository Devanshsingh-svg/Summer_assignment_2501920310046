def number_pyramid(rows: int) -> None:
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        for j in range(1, i + 1): print(j, end="")
        for j in range(i - 1, 0, -1): print(j, end="")
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    number_pyramid(rows)
