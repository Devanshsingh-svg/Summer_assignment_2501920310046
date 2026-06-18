def sort_descending(arr: list[int]) -> list[int]:
    return sorted(arr, reverse=True)

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print(f"Array sorted descending: {sort_descending(arr)}")
