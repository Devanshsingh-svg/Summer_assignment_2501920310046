def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    res = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res.append(arr1[i]); i += 1
        else:
            res.append(arr2[j]); j += 1
    res.extend(arr1[i:])
    res.extend(arr2[j:])
    return res

if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]
    print(f"Merged sorted: {merge_sorted_arrays(arr1, arr2)}")
