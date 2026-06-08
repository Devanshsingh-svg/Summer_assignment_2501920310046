def print_repeated_number_pattern(rows: int) -> None:
    for i in range(1, rows + 1):
        print(str(i) * i)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    print_repeated_number_pattern(rows)
