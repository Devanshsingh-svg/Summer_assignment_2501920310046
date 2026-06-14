def element_frequency(arr: list[int]) -> dict[int, int]:
    freq = {}
    for x in arr: freq[x] = freq.get(x, 0) + 1
    return freq

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print(f"Frequencies: {element_frequency(arr)}")
