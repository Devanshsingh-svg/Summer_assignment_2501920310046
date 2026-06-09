def hollow_square_pattern(size: int) -> None:
    for i in range(size):
        if i == 0 or i == size - 1:
            print("*" * size)
        else:
            print("*" + " " * (size - 2) + "*")

if __name__ == "__main__":
    size = int(input("Enter size of square: "))
    hollow_square_pattern(size)
