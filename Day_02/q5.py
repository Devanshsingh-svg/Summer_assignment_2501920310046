def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(abs(n)))

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Sum of digits of {n} is: {sum_of_digits(n)}")
