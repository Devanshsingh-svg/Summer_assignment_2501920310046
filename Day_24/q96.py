def remove_duplicate_chars(s: str) -> str:
    res = []
    seen = set()
    for c in s:
        if c not in seen:
            res.append(c)
            seen.add(c)
    return "".join(res)

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Without duplicates: {remove_duplicate_chars(s)}")
