def quiz_app():
    score = 0
    print("Q1: What is the capital of France?")
    if input("Answer: ").strip().lower() == "paris":
        print("Correct!")
        score += 1
    else: print("Wrong.")
    print(f"Your total score is: {score}")

if __name__ == "__main__":
    # quiz_app()
    print("Quiz application ready.")
