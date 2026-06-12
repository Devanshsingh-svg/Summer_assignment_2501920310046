def is_perfect(n: int) -> bool:
    if n <= 0: return False
    return sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"{n} is perfect: {is_perfect(n)}")
