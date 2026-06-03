def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"GCD of {a} and {b} is: {gcd(a, b)}")
