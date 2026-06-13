def count_even_odd(arr: list[int]) -> tuple[int, int]:
    even = sum(1 for x in arr if x % 2 == 0)
    return even, len(arr) - even

if __name__ == "__main__":
    arr = list(map(int, input("Enter space separated array elements: ").split()))
    e, o = count_even_odd(arr)
    print(f"Even count: {e}, Odd count: {o}")
