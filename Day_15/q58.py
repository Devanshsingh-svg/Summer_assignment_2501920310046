def rotate_left(arr: list[int], k: int) -> list[int]:
    if not arr: return arr
    k %= len(arr)
    return arr[k:] + arr[:k]

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter rotate count: "))
    print(f"Left rotated array: {rotate_left(arr, k)}")
