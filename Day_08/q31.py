def print_character_triangle(rows: int) -> None:
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    print_character_triangle(rows)
