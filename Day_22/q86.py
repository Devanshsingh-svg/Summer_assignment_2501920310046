def count_words(s: str) -> int:
    return len(s.split())

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    print(f"Word count: {count_words(s)}")
