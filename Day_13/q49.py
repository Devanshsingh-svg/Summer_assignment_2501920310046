def display_array(arr: list[int]) -> None:
    print(f"Array elements: {arr}")

if __name__ == "__main__":
    arr = list(map(int, input("Enter space separated array elements: ").split()))
    display_array(arr)
