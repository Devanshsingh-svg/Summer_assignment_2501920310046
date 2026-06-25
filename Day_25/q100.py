def sort_words_by_length(s: str) -> list[str]:
    return sorted(s.split(), key=len)

if __name__ == "__main__":
    s = input("Enter a sentence: ")
    print(f"Sorted by length: {sort_words_by_length(s)}")
