def reverse_star_pattern(rows: int) -> None:
    for i in range(rows, 0, -1):
        print("*" * i)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    reverse_star_pattern(rows)
