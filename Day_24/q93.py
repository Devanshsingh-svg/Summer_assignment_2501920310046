def check_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2): return False
    return s2 in (s1 + s1)

if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print(f"Is rotation: {check_rotation(s1, s2)}")
