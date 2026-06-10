def reverse_pyramid(rows: int) -> None:
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    reverse_pyramid(rows)
