def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print(f"Are anagrams: {are_anagrams(s1, s2)}")
