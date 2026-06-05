def is_perfect(n: int) -> bool:
    if n <= 0: return False
    divisors_sum = sum(i for i in range(1, n // 2 + 1) if n % i == 0)
    return divisors_sum == n

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_perfect(n): print(f"{n} is a perfect number.")
    else: print(f"{n} is not a perfect number.")
