def is_palindrome(n: int) -> bool:
    return str(abs(n)) == str(abs(n))[::-1]

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if is_palindrome(n):
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")
