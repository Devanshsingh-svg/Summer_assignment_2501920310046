def count_vowels_consonants(s: str) -> tuple[int, int]:
    vowels = set("aeiouAEIOU")
    v = sum(1 for c in s if c in vowels)
    c = sum(1 for c in s if c.isalpha() and c not in vowels)
    return v, c

if __name__ == "__main__":
    s = input("Enter a string: ")
    v, c = count_vowels_consonants(s)
    print(f"Vowels: {v}, Consonants: {c}")
