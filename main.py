import random

# Variables

userInput = input("Rock, Paper or Scissors?: ")
points = 0
computerPoints = 0

# Actions & Computer choice

possibleActions = ["Rock", "Paper", "Scissors"]
computerAction = random.choice(possibleActions).lower()

for i in range(len(possibleActions)):
    possibleActions[i] = possibleActions[i].lower()

if (userInput.lower() in possibleActions):
    print(f"\nYou picked {userInput.title()}, and the computer picked {computerAction.title()} \n")

# Make Scissor = Scissors

if userInput.lower() == "scissor":
    userInput = "scissors"

# Error checker

if (userInput.lower() not in possibleActions):
    while (userInput.lower() not in possibleActions):
        print("Invalid Input, try again\n")

        userInput = input("Rock, Paper or Scissors?: ")

        if userInput.lower() in possibleActions:
            print(f"\nYou picked {userInput.title()}, and the computer picked {computerAction.title()} \n")

# The main game itself

while True:
    if userInput.lower() == computerAction:
        print(f"Both players picked {computerAction.title()}. It's a tie!")
    elif userInput.lower() == "rock":
        if computerAction == "Scissors":
            print("You won! Rock smashes Scissors. 1 point awarded")
            points += 1
        else:
            print("Paper covers rock! You lost. No point awarded")
    elif userInput.lower() == "paper":
        if computerAction == "Rock":
            print("You win! Paper covers Rock. 1 point awarded")
            points += 1
        else:

            print("Scissors cuts paper! You lost. No point awarded")
    elif userInput.lower() == "scissors":
        if computerAction == "Paper":
            print("You win! Scissors cuts paper. 1 point awarded")
            points += 1
        else:
            print("Rock smashes Scissors! You lost. No point awarded")

    playAgain = input("Play again? (y/n): ")
    print()
    if playAgain.lower() == "yes" or playAgain.lower() == "y":
        userInput = input("Rock, Paper or Scissors?: ")
        possibleActions = ["Rock", "Paper", "Scissors"]
        computerAction = random.choice(possibleActions)
        print(f"\nYou picked {userInput}, and the computer picked {computerAction} \n")

        if userInput.lower() == "scissor":
            userInput == "scissors"

    else:
        print("Thanks for playing with me!")
        break
