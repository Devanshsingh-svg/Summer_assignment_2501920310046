def reverse_number(n: int) -> int:
    sign = -1 if n < 0 else 1
    reversed_n = int(str(abs(n))[::-1])
    return sign * reversed_n

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Reversed number of {n} is: {reverse_number(n)}")
