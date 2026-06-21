def to_uppercase(s: str) -> str:
    res = []
    for c in s:
        if 'a' <= c <= 'z':
            res.append(chr(ord(c) - 32))
        else:
            res.append(c)
    return "".join(res)

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Uppercase: {to_uppercase(s)}")
