def remove_spaces(s: str) -> str:
    return "".join(c for c in s if c != " ")

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Without spaces: {remove_spaces(s)}")
