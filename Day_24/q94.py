def compress_string(s: str) -> str:
    if not s: return ""
    res, count = [], 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]: count += 1
        else:
            res.append(s[i-1] + str(count))
            count = 1
    res.append(s[-1] + str(count))
    compressed = "".join(res)
    return compressed if len(compressed) < len(s) else s

if __name__ == "__main__":
    s = input("Enter a string: ")
    print(f"Compressed: {compress_string(s)}")
