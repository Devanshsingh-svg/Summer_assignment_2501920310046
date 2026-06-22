def char_frequency(s: str) -> dict[str, int]:
    freq = {}
    for c in s: freq[c] = freq.get(c, 0) + 1
    return freq

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Frequencies: {char_frequency(s)}")
