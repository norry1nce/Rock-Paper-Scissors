import random

choices = ["rock", "paper", "scissors"]


def get_choice():
    choice = input("Choose between rock, paper and scissors! : ").lower()
    while choice not in choices:
        choice = input(
            "Invalid choice of set! Choose between rock, paper and scissors! : "
        )
    return choice


def decide_win(user, com):
    if user == com:
        return "tie"

    elif user == "paper" and com == "rock":
        return "won"
    elif user == "rock" and com == "scissors":
        return "won"
    elif user == "scissors" and com == "paper":
        return "won"

    else:
        return "lose"


playing = "yes"

while playing == "yes":

    player_score = 0
    com_score = 0

    print("Welcome to rock, paper, and scissors!")

    while player_score < 3 and com_score < 3:

        user = get_choice()
        com = random.choice(choices)

        print(f"Computer chooses {com}!")

        deciding = decide_win(user, com)

        if deciding == "tie":
            print(f"Player chooses {user} and Computer chooses {com}! It was a tie!")
        elif deciding == "won":
            print(f"Player chooses {user} and Computer chooses {com}! You won a round!")
            player_score += 1
        elif deciding == "lose":
            print(
                f"Player chooses {user} and Computer chooses {com}! You lost a round!"
            )
            com_score += 1

        print(f"Your score : {player_score} / Computer score: {com_score}")

    if player_score >= 3:
        print("You won the game!")
    else:
        print("Computer won! You lost the game!")

    playing = input("Play again? Yes/No : ").lower()
