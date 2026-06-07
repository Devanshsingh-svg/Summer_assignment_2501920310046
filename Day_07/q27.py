def recursive_sum_of_digits(n: int) -> int:
    n = abs(n)
    if n == 0: return 0
    return (n % 10) + recursive_sum_of_digits(n // 10)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Sum of digits of {n} is: {recursive_sum_of_digits(n)}")
