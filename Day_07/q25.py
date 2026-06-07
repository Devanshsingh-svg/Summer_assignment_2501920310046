def recursive_factorial(n: int) -> int:
    if n < 0: raise ValueError("Negative numbers not allowed.")
    if n == 0 or n == 1: return 1
    return n * recursive_factorial(n - 1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Factorial of {n} is: {recursive_factorial(n)}")
