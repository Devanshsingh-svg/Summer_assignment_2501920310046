def merge_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    return arr1 + arr2

if __name__ == "__main__":
    arr1 = list(map(int, input("Enter array 1 elements: ").split()))
    arr2 = list(map(int, input("Enter array 2 elements: ").split()))
    print(f"Merged array: {merge_arrays(arr1, arr2)}")
