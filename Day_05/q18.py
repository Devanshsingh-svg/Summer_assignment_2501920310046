def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1): res *= i
    return res

def is_strong(n: int) -> bool:
    if n <= 0: return False
    return sum(factorial(int(d)) for d in str(n)) == n

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_strong(n): print(f"{n} is a strong number.")
    else: print(f"{n} is not a strong number.")
