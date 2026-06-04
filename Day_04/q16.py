from q15 import is_armstrong

def print_armstrong_in_range(start: int, end: int) -> None:
    armstrongs = [n for n in range(start, end + 1) if is_armstrong(n)]
    print(f"Armstrong numbers between {start} and {end}: {armstrongs}")

if __name__ == "__main__":
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print_armstrong_in_range(start, end)
