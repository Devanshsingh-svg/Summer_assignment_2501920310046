def recursive_fibonacci(n: int) -> int:
    if n <= 0: raise ValueError("Must be positive.")
    if n == 1: return 0
    if n == 2: return 1
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"The {n}th Fibonacci term is: {recursive_fibonacci(n)}")
