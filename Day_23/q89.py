def first_non_repeating(s: str) -> str:
    freq = {}
    for c in s: freq[c] = freq.get(c, 0) + 1
    for c in s:
        if freq[c] == 1: return c
    return ""

if __name__ == "__main__":
    s = input("Enter a string: ")
    res = first_non_repeating(s)
    print(f"First non-repeating char: {res}" if res else "None found")
