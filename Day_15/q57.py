def reverse_array(arr: list[int]) -> list[int]:
    return arr[::-1]

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print(f"Reversed array: {reverse_array(arr)}")
