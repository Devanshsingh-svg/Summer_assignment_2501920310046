def print_factors(n: int) -> None:
    factors = [i for i in range(1, n + 1) if n % i == 0]
    print(f"Factors of {n}: {factors}")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print_factors(n)
