def first_repeating(s: str) -> str:
    seen = set()
    for c in s:
        if c in seen: return c
        seen.add(c)
    return ""

if __name__ == "__main__":
    s = input("Enter a string: ")
    res = first_repeating(s)
    print(f"First repeating char: {res}" if res else "None found")
