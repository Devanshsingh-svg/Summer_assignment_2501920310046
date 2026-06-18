def binary_search(arr: list[int], target: int) -> int:
    arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))
    idx = binary_search(arr.copy(), target)
    print(f"Element found at index {idx} in sorted array" if idx != -1 else "Element not found")
