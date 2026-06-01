def factorial(n: int) -> int:
    if n < 0: raise ValueError("Factorial is not defined for negative numbers.")
    res = 1
    for i in range(1, n + 1): res *= i
    return res

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Factorial of {n} is: {factorial(n)}")
