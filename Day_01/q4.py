def count_digits(n: int) -> int:
    return len(str(abs(n)))

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Number of digits in {n} is: {count_digits(n)}")
