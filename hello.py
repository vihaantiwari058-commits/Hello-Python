print("hello World")
print("Welcome to the number guessing game!")
import random 

answer = random.randrange(1, 101)
chances = 0 
print("You have 10 chances to guess the number between 1 and 100.")

while chances < 10:
    guess = int(input("Enter your guess: "))
    chances += 1

    if guess < answer:
        print("Your guess is too low.")
    elif guess > answer:
        print("Your guess is too high.")
    else:
        print(f"Congratulations! You've guessed the number {answer} in {chances} chances.")
        break

    if chances == 10 and guess != answer:
    print(f"""Sorry, you've used all your chances and failed to guess the number. 
        The correct number was {answer}.""") 
