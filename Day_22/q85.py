def is_palindrome_string(s: str) -> bool:
    return s == s[::-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Is palindrome: {is_palindrome_string(s)}")
