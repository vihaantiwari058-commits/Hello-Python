print("Hello, World!")
print("Welcome to the number guessing game!")
import random

answer = random.randint(1, 100)
chances = 1 
print("You have 10 chances to guess the number between 1 and 100.")

while chances < 10:
    guess = int(input("Enter your guess: "))
    chances += 1 

    if guess < answer:
        print("your guess is too low.")
     elif guess > answer:
        print("your guess is too high.")
     else:
        print(f"Congratulations! You've guessed the number {answer} in {chances - 1} chances.")
        break 

     if chances == 10:
        print(f"""Sorry, you've used all your chances. the correct number was {answer} Better luck next time !""")
             The correct number was {answer}. Better luck next time!""")
             Thank you for playing the number guessing game! 