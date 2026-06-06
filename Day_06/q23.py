def count_set_bits(n: int) -> int:
    return bin(n).count("1")

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(f"Number of set bits in {n} is: {count_set_bits(n)}")
