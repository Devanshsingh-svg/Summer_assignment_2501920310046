def fibonacci_series(n: int) -> list[int]:
    if n <= 0: return []
    if n == 1: return [0]
    fib = [0, 1]
    for _ in range(2, n): fib.append(fib[-1] + fib[-2])
    return fib

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(f"Fibonacci series: {fibonacci_series(n)}")
