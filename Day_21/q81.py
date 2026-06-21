def string_length(s: str) -> int:
    count = 0
    for _ in s: count += 1
    return count

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Length: {string_length(s)}")
