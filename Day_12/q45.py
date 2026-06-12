def is_palindrome(n: int) -> bool:
    return str(abs(n)) == str(abs(n))[::-1]

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"{n} is palindrome: {is_palindrome(n)}")
