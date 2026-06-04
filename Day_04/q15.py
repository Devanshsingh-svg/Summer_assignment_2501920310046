def is_armstrong(n: int) -> bool:
    s = str(abs(n))
    power = len(s)
    return sum(int(digit) ** power for digit in s) == abs(n)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_armstrong(n): print(f"{n} is an Armstrong number.")
    else: print(f"{n} is not an Armstrong number.")
