def second_largest(arr: list[int]) -> int:
    unique_arr = list(set(arr))
    unique_arr.sort(reverse=True)
    return unique_arr[1] if len(unique_arr) > 1 else None

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    res = second_largest(arr)
    print(f"Second largest: {res}" if res is not None else "No second largest found")
