from q9 import is_prime

def print_primes_in_range(start: int, end: int) -> None:
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    print(f"Primes between {start} and {end}: {primes}")

if __name__ == "__main__":
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print_primes_in_range(start, end)
