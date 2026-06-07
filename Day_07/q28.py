def recursive_reverse_number(n: int, rev: int = 0) -> int:
    if n == 0: return rev
    return recursive_reverse_number(n // 10, rev * 10 + (n % 10))

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    sign = -1 if n < 0 else 1
    print(f"Reversed number is: {sign * recursive_reverse_number(abs(n))}")
