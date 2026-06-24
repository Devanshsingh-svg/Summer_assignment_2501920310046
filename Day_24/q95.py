def longest_word(s: str) -> str:
    words = s.split()
    return max(words, key=len) if words else ""

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    print(f"Longest word: {longest_word(s)}")
