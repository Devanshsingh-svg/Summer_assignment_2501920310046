def reverse_string(s: str) -> str:
    return s[::-1]

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Reversed: {reverse_string(s)}")
