def print_half_pyramid(rows: int) -> None:
    for i in range(1, rows + 1):
        print("*" * i)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    print_half_pyramid(rows)
