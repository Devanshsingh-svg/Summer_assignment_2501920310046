import random
def guessing_game():
    target = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < target: print("Too low!")
            elif guess > target: print("Too high!")
            else:
                print("Congratulations! You guessed it.")
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    # guessing_game()
    print("Number guessing game ready.")
