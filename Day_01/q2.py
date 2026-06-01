def print_multiplication_table(number: int, up_to: int = 10) -> None:
    print(f"\n=== Multiplication Table for {number} ===")
    for i in range(1, up_to + 1):
        product = number * i
        print(f"{number} x {i:2d} = {product}")

if __name__ == "__main__":
    try:
        user_input = input("Enter a number to print its multiplication table: ")
        target_number = int(user_input)
        print_multiplication_table(target_number)
    except ValueError:
        print("❌ Error: Invalid input. Please enter a whole number (integer) only.")