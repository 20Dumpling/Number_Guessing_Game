import random

# returns a randomly selected number from the provided endpoint
number_to_be_guessed = random.randrange(100)

count = 0
number_of_guesses = 7

print(f"Welcome to lain's guessing game! You have a total of {number_of_guesses} guesses available.")
input("Press Enter to start the game...")

while count < number_of_guesses:
    count+=1
    players_guess = int(input("Enter your guess: ").strip())
    if (players_guess == number_to_be_guessed):
        print("You found it!")
        break

    elif (players_guess > number_to_be_guessed):
        print("You guessed too high!")

    elif (players_guess < number_to_be_guessed):
        print("You guessed too low!")
else:
    # runs only if the user guesses wrong and loop does not hit the break; part of the loop but not inside it
    print(f"Ouch... missed out this game, the number is {number_to_be_guessed}. Try better next time, stay hard:))")