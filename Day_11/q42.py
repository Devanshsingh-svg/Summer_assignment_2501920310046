def find_max(a: int, b: int) -> int:
    return a if a > b else b

if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"Max: {find_max(a, b)}")
