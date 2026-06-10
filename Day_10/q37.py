def print_star_pyramid(rows: int) -> None:
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    print_star_pyramid(rows)
