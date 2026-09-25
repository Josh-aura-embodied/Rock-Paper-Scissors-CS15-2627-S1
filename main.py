import random


def get_cpu_choice():
    """Generates a random choice for the CPU."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def get_player_choice():
    """Prompts the user for a choice and validates the input."""
    valid_choices = ["rock", "paper", "scissors"]
    while True:
        # Using .lower() to handle cases like "Rock" or "ROCK"
        choice = input("Enter rock, paper, or scissors: ").strip().lower()
        if choice in valid_choices:
            return choice
        print("Invalid input. Please try again.")


def check_winner(cpu_choice, player_choice):
    """Determines the winner of a single round."""
    if player_choice == cpu_choice:
        return "TIE"

    if cpu_choice == "rock":
        if player_choice == "paper":
            return "PLAYER"
        else:
            return "CPU"
    elif cpu_choice == "paper":
        if player_choice == "scissors":
            return "PLAYER"
        else:
            return "CPU"
    elif cpu_choice == "scissors":
        if player_choice == "rock":
            return "PLAYER"
        else:
            return "CPU"


def play_round():
    """Executes a single complete round and returns the winner."""
    cpu = get_cpu_choice()
    player = get_player_choice()

    print(f"CPU chose: {cpu}")
    print(f"You chose: {player}")

    winner = check_winner(cpu, player)
    return winner


def start_tournament():
    """Runs a Best-of-5 tournament (first to 3 wins)."""
    player_wins = 0
    cpu_wins = 0
    ties = 0

    print("=== Welcome to the goat Josh's Rock, Paper, Scissors Tournament! ===")
    print("First to 3 wins takes the crown.\n")

    # Loop continues until either the player or CPU reaches 3 wins
    while player_wins < 3 and cpu_wins < 3:
        winner = play_round()

        if winner == "PLAYER":
            print("Result: You win this round!")
            player_wins += 1
        elif winner == "CPU":
            print("Result: CPU wins this round!")
            cpu_wins += 1
        else:
            print("Result: It's a tie!")
            ties += 1

        # Display current score after every round
        print(f"Current Score -> Player: {player_wins} | CPU: {cpu_wins} | Ties: {ties}\n")
        print("-" * 40)

    # Display the overall winner
    if player_wins == 3:
        print(" OVERALL WINNER: PLAYER! Congratulations! ")
    else:
        print(" OVERALL WINNER: CPU! Better luck next time. ")


# Execute the program
if __name__ == "__main__":
    start_tournament()