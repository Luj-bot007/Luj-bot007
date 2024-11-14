#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Owner
#
# Created:     20-05-2024
# Copyright:   (c) Owner 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def main():
    print("Welcome to the number of guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1,100)

    guess_count=0

    while True:
        guess = input("Enter your guess:")

        try:
            guess=int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue

        guess_count+= 1

        if guess < number_to_guess:
            print("TOO LOW!")
        elif guess > number_to_guess:
            print("TOO HIGH")
        else:
            print(f"Congrats")
            break

if __name__ == "__main__":
    main()

