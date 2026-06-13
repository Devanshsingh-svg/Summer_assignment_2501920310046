def sum_and_average(arr: list[int]) -> tuple[int, float]:
    total = sum(arr)
    return total, total / len(arr) if arr else 0.0

if __name__ == "__main__":
    arr = list(map(int, input("Enter space separated array elements: ").split()))
    s, avg = sum_and_average(arr)
    print(f"Sum: {s}, Average: {avg}")
