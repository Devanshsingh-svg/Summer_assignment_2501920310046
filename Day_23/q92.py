def max_occurring_char(s: str) -> str:
    if not s: return ""
    freq = {}
    for c in s: freq[c] = freq.get(c, 0) + 1
    return max(freq, key=freq.get)

if __name__ == "__main__":
    s = input("Enter a string: ")
    res = max_occurring_char(s)
    print(f"Max occurring char: {res}" if res else "String empty")
