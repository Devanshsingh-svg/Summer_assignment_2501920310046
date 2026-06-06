def decimal_to_binary(n: int) -> str:
    return bin(n).replace("0b", "")

if __name__ == "__main__":
    n = int(input("Enter a decimal number: "))
    print(f"Binary of {n} is: {decimal_to_binary(n)}")
