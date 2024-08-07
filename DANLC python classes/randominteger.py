"""Create a simple number guessing game where the computer randomly selects a number between 1 and 100, and the user has to guess it. Use a while loop to keep asking the user for guesses until they guess the correct number. Provide feedback if the guess is too high or too low."""




import random

# Generate a random number between 1 and 100
target_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Initialize the number of attempts
attempts = 0

while True:
    # Ask the user for their guess
    guess = input("Enter your guess: ")
    
    # Validate input
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    attempts += 1
    
    # Check if the guess is correct
    if guess == target_number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < target_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
