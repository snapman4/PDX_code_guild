import random

print("Let's play rock paper scissors!")

def user_choice():
    r_p_s = input("Make a selection of rock, paper or scissors: ")
    r_p_s = r_p_s.lower()
    return r_p_s


def computer_choice():
    options = ["rock", "paper", "scissors"]
    computer_select = random.choice(options)
    return computer_select


# print("You selected: {}".format(user_choice()))
# print("The computer selected: {}".format(computer_choice()))

user_choice = user_choice()
computer_choice = computer_choice()

def outcome():
    if user_choice == "rock":
        if computer_choice == "rock":
            return "Tie"
        elif computer_choice == "paper":
            return "You Lose"
        else:
            return "You win!"
    elif user_choice == "paper":
        if computer_choice == "rock":
            return "You win!"
        elif computer_choice == "paper":
            return "Tie"
        else:
            return "You Lose"
    else:
        if computer_choice == "rock":
            return "You lose"
        elif computer_choice == "paper":
            return "You win!"
        else:
            return "Tie"

print("You selected: {}".format(user_choice))
print("The computer selected: {}".format(computer_choice))

print(outcome())
