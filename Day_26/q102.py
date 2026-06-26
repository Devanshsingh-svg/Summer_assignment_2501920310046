def voting_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age >= 18: print("You are eligible to vote.")
        else: print("You are not eligible to vote yet.")
    except ValueError:
        print("Invalid age.")

if __name__ == "__main__":
    # voting_eligibility()
    print("Voting eligibility system ready.")
