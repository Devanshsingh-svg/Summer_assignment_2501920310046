def largest_prime_factor(n: int) -> int:
    i = 2
    largest = -1
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 1
    if n > 1:
        largest = n
    return largest

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Largest prime factor of {n} is: {largest_prime_factor(n)}")
