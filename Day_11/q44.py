def find_factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1): res *= i
    return res

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Factorial of {n} is: {find_factorial(n)}")
