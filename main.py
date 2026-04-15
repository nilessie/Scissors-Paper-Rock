import random


class Player:
    def __init__(self, name):
        self.player_name = name
        self.choice = None
        self.wins = 0
        self.loses = 0
        self.ties = 0

class SPR:
    def __init__(self, id, name, symbol):
        self.id = id
        self.name = name
        self.symbol = symbol


def main():
    num_games = 0

    while True:
        try:
            num_games = int(input("Enter a number of how many games to play: "))
            if num_games <= 0:
                print(f"Input must be greater then 0")
            else:
                break
        except ValueError:
            print("Input must be a number")

    num_games_copy = num_games
    round_num = 1
    accepted_choices = ["s", "p", "r"]
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    
    # MAIN GAME LOOP
    while num_games != 0:
        # Gets the choice of player and computer
        print(f"\nRound: {round_num}")
        player_choice = str(input("\nChoose one:\nScissors [S]\nPaper [P]\nRock [R]\n\n# "))
        computer_choice = accepted_choices[random.randint(0, 2)]
        
        # Makes sure the player input is valid.
        try:
            formatted_player_choice = player_choice[0].lower()
            if formatted_player_choice.isalpha() != True or formatted_player_choice not in accepted_choices:
                print(f"Input '{formatted_player_choice}' not valid. Valid inputs are S, P, or R")
                continue
        except Exception as e:
            print(f"Input '{player_choice}' not valid. Valid inputs are S, P, or R")
            continue

        player1.choice = class_assigner(formatted_player_choice)
        player2.choice = class_assigner(computer_choice)

        game_verdict = winner_validator(player1, player2)
        if game_verdict is None:
            print(f"{player1.choice.name} {player1.choice.symbol}  and {player2.choice.name} {player1.choice.symbol} . It's a TIE! ")
            write_round_results(game_verdict, round_num)
        elif game_verdict.player_name == player1.player_name:
            write_round_results(game_verdict, round_num)
            print(f"{player1.choice.name} {player1.choice.symbol}  beats {player2.choice.name} {player2.choice.symbol}. Player 1 wins!")
        else:
            write_round_results(game_verdict, round_num)
            print(f"{player2.choice.name} {player2.choice.symbol}  beats {player1.choice.name} {player1.choice.symbol}. Player 2 wins!")

        num_games -= 1
        round_num += 1

    write_game_results(player1, player2, num_games_copy)


# Assign a object to the player choices
def class_assigner(choice):
    if choice == "s":
        choice = SPR(id= 0, name="Scissors", symbol="✂️")
    elif choice == "p":
        choice = SPR(id= 1, name="Paper", symbol="📄")
    else:
        choice = SPR(id= 2, name="Rock", symbol="🪨")
    
    return choice


# Compares the choices made and returns the results
def winner_validator(player1, player2):
    # Player 1 wins
    if (
        player1.choice.id == 0 and player2.choice.id == 1 or
        player1.choice.id == 1 and player2.choice.id == 2 or
        player1.choice.id == 2 and player2.choice.id == 0
        ):
        player1.wins += 1
        player2.loses += 1
        return player1
    # Player 2 wins
    elif (
        player2.choice.id == 0 and player1.choice.id == 1 or
        player2.choice.id == 1 and player1.choice.id == 2 or
        player2.choice.id == 2 and player1.choice.id == 0
        ):
        player2.wins += 1
        player1.loses += 1
        return player2
    # Tie
    else:
        player1.ties += 1
        player2.ties += 1
        return None


# Writes the results for the round
def write_round_results(game_verdict, round_num):
    if game_verdict == None:
        with open("results.txt", "a") as f:
            f.write(f"Round {round_num}: Tied\n")
    else:
        with open("results.txt", "a") as f:
            f.write(f"Round {round_num} winner: {game_verdict.player_name}\n")


# Writes the results of the entire game
def write_game_results(player1, player2, num_games):
    results1 = f"{player1.player_name} Stats\nWins: {player1.wins}\nLoses: {player1.loses}\nTies: {player1.ties}"
    results2 = f"{player1.player_name} Stats\nWins: {player2.wins}\nLoses: {player2.loses}\nTies: {player2.ties}"
    
    with open("results.txt", "a") as f:
        f.write(f"\n----- GAME RESULTS -----\n{results1}\n\n{results2}\n------------------------\n\n")
    print(f"\n----- GAME RESULTS -----\n{results1}\n\n{results2}\n------------------------\n\n")


main()

