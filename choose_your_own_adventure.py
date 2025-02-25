name = input("Type your name to begin the game: ")
print(f"Welcome {name} to the adventure!")

answer = input(
    "You are on a dirt road, it has come to an end so you have to either go left or right. Type left to go to left OR type right to go to right: ").lower()

if answer == "left":
    answer = input(
        "You come to a river. You can either walk around it or swim it. Type walk to walk around OR swim to swim across: ").lower()

    if answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    elif answer == "swim":
        print("You swam across and eaten by an alligator.")
    else:
        print("Not a valid option. You lose!")
elif answer == "right":
    answer = input("You come to a bridge. Type in cross or back: ").lower()

    if answer == "back":
        print("You should have crossed the bridge. You lose!")
    elif answer == "cross":
        answer = input("You met a stranger. Talk to him? Yes/No: ").lower()

        if answer == "yes":
            print("You got a map. You win!")
        elif answer == "no":
            print("You lost the way to the treasure. You lost!")
        else:
            print("Not a valid option. You lose!")
    else:
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose!")

print(f"Thank you for playing, {name}.")
