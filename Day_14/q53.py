def linear_search(arr: list[int], target: int) -> int:
    for i, val in enumerate(arr):
        if val == target: return i
    return -1

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target to search: "))
    idx = linear_search(arr, target)
    print(f"Element found at index {idx}" if idx != -1 else "Element not found")
