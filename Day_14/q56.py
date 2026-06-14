def find_duplicates(arr: list[int]) -> list[int]:
    seen = set()
    dupes = set()
    for x in arr:
        if x in seen: dupes.add(x)
        seen.add(x)
    return list(dupes)

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print(f"Duplicates: {find_duplicates(arr)}")
