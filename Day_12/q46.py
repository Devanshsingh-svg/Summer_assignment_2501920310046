def is_armstrong(n: int) -> bool:
    s = str(abs(n))
    return sum(int(d)**len(s) for d in s) == abs(n)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"{n} is Armstrong: {is_armstrong(n)}")
