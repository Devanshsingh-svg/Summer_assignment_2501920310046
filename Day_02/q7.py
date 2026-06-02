def product_of_digits(n: int) -> int:
    prod = 1
    for digit in str(abs(n)):
        prod *= int(digit)
    return prod

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Product of digits of {n} is: {product_of_digits(n)}")
