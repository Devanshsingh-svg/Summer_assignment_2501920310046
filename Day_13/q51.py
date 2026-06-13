def min_max(arr: list[int]) -> tuple[int, int]:
    return (min(arr), max(arr)) if arr else (None, None)

if __name__ == "__main__":
    arr = list(map(int, input("Enter space separated array elements: ").split()))
    mini, maxi = min_max(arr)
    print(f"Smallest: {mini}, Largest: {maxi}")
