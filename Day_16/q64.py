def remove_duplicates(arr: list[int]) -> list[int]:
    res = []
    seen = set()
    for x in arr:
        if x not in seen:
            res.append(x)
            seen.add(x)
    return res

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print(f"Array without duplicates: {remove_duplicates(arr)}")
