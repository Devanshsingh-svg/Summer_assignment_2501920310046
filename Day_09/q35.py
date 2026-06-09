def repeated_character_pattern(rows: int) -> None:
    for i in range(1, rows + 1):
        print(chr(64 + i) * i)

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    repeated_character_pattern(rows)
