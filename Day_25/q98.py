def common_chars(s1: str, s2: str) -> list[str]:
    return list(set(s1) & set(s2))

if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print(f"Common characters: {common_chars(s1, s2)}")
