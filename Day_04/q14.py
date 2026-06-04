def nth_fibonacci(n: int) -> int:
    if n <= 0: raise ValueError("n must be positive")
    if n == 1: return 0
    if n == 2: return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"The {n}th Fibonacci term is: {nth_fibonacci(n)}")
