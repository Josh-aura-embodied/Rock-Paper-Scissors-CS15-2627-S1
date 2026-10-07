#STILL WORKING ON IT NEEDS TO BE REDONE
import random


def get_cpu_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_player_choice():
    while True:
        choice = input("Rock, paper, or scissors? ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Nah, pick rock, paper, or scissors.")


def determine_winner(player, cpu):
    if player == cpu:
        return "tie"

    wins = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    return "player" if wins[player] == cpu else "cpu"


def start_game():
    player_score = 0
    cpu_score = 0

    print("Welcome to Josh's Rock, Paper, Scissors game.")
    print("First to 3 wins takes it.")
    print()

    while player_score < 3 and cpu_score < 3:
        cpu = get_cpu_choice()
        player = get_player_choice()

        print(f"Computer: {cpu}")
        print(f"You: {player}")

        winner = determine_winner(player, cpu)

        if winner == "player":
            player_score += 1
            print("You took that round.")
        elif winner == "cpu":
            cpu_score += 1
            print("Computer took that round.")
        else:
            print("Tie round.")

        print(f"Score - You: {player_score} | Computer: {cpu_score}")
        print()

    if player_score == 3:
        print("Game over, you won the set.")
    else:
        print("Game over, computer took the set.")


if __name__ == "__main__":
    start_game()