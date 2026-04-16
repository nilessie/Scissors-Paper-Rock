import random


class Player:
    def __init__(self, name, num_rounds):
        self.player_name = name
        self.choice = None
        self.wins = 0
        self.loses = 0
        self.ties = 0
        self.valid_input = ["r", "p", "s"]
        self.valid_symbols = ["✂️", "📄", "🪨"] 
        self.num_rounds = num_rounds
    
    # Used to demonstrate polymorphism
    def __str__(self):
        return f"{self.player_name} (W:{self.wins} L:{self.loses} T:{self.ties})"

class SPR:
    def __init__(self, id, name, symbol, beats, description):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.beats = beats
        self.description = description

    # Used to demonstrate polymorphism
    def __str__(self):
        return f"{self.symbol} {self.name}"


def main():
    # Gain the number of games the user wants to play
    while True:
        try:
            num_rounds = int(input("Enter the number of games you want to play: "))
            if num_rounds <= 0:
                print(f"Input must be greater then 0")
            else:
                break
        except ValueError:
            print("Input must be a number")

    round_num = 1
    player1 = Player("Player 1", num_rounds)
    player2 = Player("Player 2", num_rounds)

    # MAIN GAME LOOP
    while num_rounds != 0:
        
        # Gets the players choice
        print(f"\nRound: {round_num}")
        player_choice = str(input("\nChoose one:\nScissors [S]\nPaper [P]\nRock [R]\n\n# "))
        computer_choice = player2.valid_input[random.randint(0, 2)]

        # Check the players input is valid
        try:
            formatted_player_choice = player_choice[0].lower()
            if formatted_player_choice.isalpha() != True or formatted_player_choice not in player1.valid_input:
                print(f"Input '{formatted_player_choice}' not valid. Valid inputs are S, P, or R")
                continue
        except Exception as e:
            print(f"Input '{player_choice}' not valid. Valid inputs are S, P, or R")
            continue
        
        # Creates two player objects
        player1.choice = class_assigner(formatted_player_choice)
        player2.choice = class_assigner(computer_choice)

        # Compares the choices and return the results of the round
        winner_validator(player1, player2, round_num)

        num_rounds -= 1
        round_num += 1

    write_game_results(player1, player2)


# Assigns a SPD object to the player choice attribute dependening on the choice made
def class_assigner(choice):
    if choice == "s":
        choice = SPR(id=0, name="Scissors", symbol="✂️", beats=1, description="A dull pair of scissors")
    elif choice == "p":
        choice = SPR(id=1, name="Paper", symbol="📄", beats=2, description="A blank piece of paper")
    else:
        choice = SPR(id=2, name="Rock", symbol="🪨", beats=0, description="A lonely rock")
    
    return choice


# Compares the choices made and returns the results
def winner_validator(player1, player2, round_num):
    # Player 1 wins
    if player1.choice.beats == player2.choice.id:
        player1.wins += 1
        player2.loses += 1
        print(f"{player1.choice.name} {player1.choice.symbol}  beats {player2.choice.name} {player2.choice.symbol}. Player 1 wins!")
        write_round_results(player1, round_num)
        return
    # Player 2 wins
    elif player2.choice.beats == player1.choice.id:
        player2.wins += 1
        player1.loses += 1
        print(f"{player2.choice.name} {player2.choice.symbol}  beats {player1.choice.name} {player1.choice.symbol}. Player 2 wins!")
        write_round_results(player2, round_num)
        return
    # Tie
    else:
        player1.ties += 1
        player2.ties += 1
        print(f"{player1.choice.name} {player1.choice.symbol}  and {player2.choice.name} {player2.choice.symbol} . It's a TIE! ")
        write_round_results(None, round_num)
        return


# Writes the round results to a file
def write_round_results(round_winner, round_num):
    if round_winner == None:
        with open("results.txt", "a") as f:
            f.write(f"Round {round_num}: Tied\n")
    else:
        with open("results.txt", "a") as f:
            f.write(f"Round {round_num} winner: {round_winner.player_name} - {round_winner.choice.description}\n")


# Writes the game results to a file and prints results to the console 
def write_game_results(player1, player2):
    p1_results = f"{player1.player_name} Stats\nWins: {player1.wins}\nLoses: {player1.loses}\nTies: {player1.ties}"
    p2_results = f"{player2.player_name} Stats\nWins: {player2.wins}\nLoses: {player2.loses}\nTies: {player2.ties}"

    if player1.wins > player2.wins:
        winner = f"{player1.player_name} WINS!"
    elif player2.wins > player1.wins:
        winner = f"{player2.player_name} WINS!"
    else:
        winner = "It's a TIE!"

    print(f"\n----- GAME RESULTS -----\n\n{winner}\n\n{p1_results}\n\n{p2_results}\n------------------------\n\n")

    with open("results.txt", "a") as f:
        f.write(f"\n----- GAME RESULTS -----\n\n{winner}\n\n{p1_results}\n\n{p2_results}\n------------------------\n\n")
    

main()

