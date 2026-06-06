def binary_to_decimal(b: str) -> int:
    return int(b, 2)

if __name__ == "__main__":
    b = input("Enter a binary number: ")
    print(f"Decimal of {b} is: {binary_to_decimal(b)}")
