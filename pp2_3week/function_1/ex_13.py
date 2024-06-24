import random

def guess_the_number():
    
    print("Hello! What is your name?")
    name = input()
    number_to_guess = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number_of_guesses = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        number_of_guesses += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {number_of_guesses} guesses!")
            break
guess_the_number()
