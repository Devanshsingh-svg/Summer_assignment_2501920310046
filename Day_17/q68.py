def find_common_elements(arr1: list[int], arr2: list[int]) -> list[int]:
    return list(set(arr1).intersection(arr2))

if __name__ == "__main__":
    arr1 = list(map(int, input("Enter array 1 elements: ").split()))
    arr2 = list(map(int, input("Enter array 2 elements: ").split()))
    print(f"Common elements: {find_common_elements(arr1, arr2)}")
