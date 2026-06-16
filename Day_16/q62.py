def max_frequency_element(arr: list[int]) -> int:
    if not arr: return None
    freq = {}
    for x in arr: freq[x] = freq.get(x, 0) + 1
    return max(freq, key=freq.get)

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print(f"Max frequency element: {max_frequency_element(arr)}")
