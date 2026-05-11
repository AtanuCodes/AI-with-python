# Rock Paper Scissors Game
# Task:
# Create a simple Rock-Paper-Scissors game against the computer.

# Ask the user to choose: rock, paper, or scissors
# Computer randomly picks one
# Decide who wins and print the result
# Show score (Player vs Computer)
# Ask if they want to play again

# Hint: Use import random and random.choice()

import random
choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0

if player_score == 0 and computer_score == 0:
    print("Welcome to Rock-Paper-Scissors Game!")
    print("First to score 3 points wins the game.")
    
while player_score < 3 and computer_score < 3:
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

if player_score == 3:
    print("Congratulations! You won the game!")
    print(f"Your score is {player_score}")
elif computer_score == 3:
    print("Computer won the game! Better luck next time.")
    print(f"Computer score is {computer_score}")