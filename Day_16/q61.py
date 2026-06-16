def missing_number(arr: list[int]) -> int:
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements (1 to N with one missing): ").split()))
    print(f"Missing number: {missing_number(arr)}")
