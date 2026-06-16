def find_pair_with_sum(arr: list[int], target: int) -> tuple[int, int]:
    seen = set()
    for x in arr:
        if target - x in seen: return (target - x, x)
        seen.add(x)
    return None

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target sum: "))
    pair = find_pair_with_sum(arr, target)
    print(f"Pair with sum {target}: {pair}" if pair else "No pair found")
