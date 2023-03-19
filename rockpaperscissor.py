import random
option=["rock","paper","scissor"]
player=None
computer=random.choice(option)
while player not in option:
    player=input("Enter a choice:")
print(f"player:{player}")
print(f"computer:{computer}")
if player== computer:
    print(f"Both players selected {player}. It's a tie!")
elif player == "rock":
    if computer== "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player == "paper":
    if computer == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")