import random 

options = ["rock", "paper", "scissors"] 
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, or scissors): ").lower()

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
            print("it's a tie!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")

        if not input("play again? (yes/no):").lower() == "yes":
            running = False

print("Thanks for playing!")
