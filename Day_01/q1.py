def sum_of_natural_numbers_fast(n: int) -> int:
    """
    Calculates the sum of the first N natural numbers using the direct formula.
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if n < 0:
        raise ValueError("Natural numbers must be non-negative integers.")
        
    # Using floor division (//) to ensure the output remains an integer type
    return (n * (n + 1)) // 2

# Example Usage:
if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    print(f"Sum of first {n} natural numbers is: {sum_of_natural_numbers_fast(n)}")