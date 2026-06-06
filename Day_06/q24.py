def power(x: float, n: int) -> float:
    res = 1.0
    abs_n = abs(n)
    for _ in range(abs_n):
        res *= x
    return res if n >= 0 else 1 / res

if __name__ == "__main__":
    x = float(input("Enter x: "))
    n = int(input("Enter n: "))
    print(f"{x}^{n} is: {power(x, n)}")
