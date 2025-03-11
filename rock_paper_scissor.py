import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to Quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid choice!")

    # random_number = random.randint(0, 2)  # rock = 0, paper = 1, scissor = 2
    # computer_pick = options[random_number]
    computer_pick = random.choice(options)
    print(f"You picked {user_input}.")
    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("Tie!")
    elif (
            (user_input == "rock" and computer_pick == "scissor") or
            (user_input == "paper" and computer_pick == "rock") or
            (user_input == "scissor" and computer_pick == "paper")):
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"The Computer won {computer_wins} times.")

if user_wins > computer_wins:
    print("Well Played!")
elif user_wins == computer_wins:
    print("It's a tie game.")
else:
    print("Better luck next time!")