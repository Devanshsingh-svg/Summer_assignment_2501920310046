def move_zeroes(arr: list[int]) -> list[int]:
    non_zeroes = [x for x in arr if x != 0]
    zeroes = [0] * (len(arr) - len(non_zeroes))
    return non_zeroes + zeroes

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    print(f"Array after moving zeroes: {move_zeroes(arr)}")
