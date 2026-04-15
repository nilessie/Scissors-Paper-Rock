import random

# RULES # 
## Rock beats Scissors
## Scissors beats Paper
## Paper beats Rock
## If both players create the same formation, then the game is a tie or draw.


class SPR:
    def __init__(self, id, name, symbol):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.wins = 0
        self.loses = 0
        self.ties = 0
        #winning_conditions = None
    

def main():
    #num_games = input("Best of how many games: ")
    while True:
        player_choice = input("Choose Scissors [S], Paper [P], or Rock [R]: ")
        computer_choice = random.randint(0, 2)

        player1 = class_assigner(player_choice)
        player2 = class_assigner(computer_choice)

        game_verdict = winner_validator(player1, player2)
        if game_verdict is None:
            print(f"{player1.name} and {player2.name}. It's a TIE! ")
        elif game_verdict is player1:
            print(f"{player1.name} beats {player2.name}. Player 1 wins!")
        else:
            print(f"{player2.name} beats {player1.name}. Player 2 wins!")



# Assign a object to the player choices
def class_assigner(choice):
    if choice == 0:
        choice = SPR(id= 0, name="Scissors", symbol="✂️")
    elif choice == 1:
        choice = SPR(id= 1, name="Paper", symbol="📄")
    else:
        choice = SPR(id= 2, name="Rock", symbol="🪨")
    
    return choice


# Compare the choices and declare a winner
def winner_validator(player1, player2):
    winner = None
    # Player 1 wins
    if (
        player1.id == 0 and player2.id == 1 or
        player1.id == 1 and player2.id == 2 or
        player1.id == 2 and player2.id == 0
        ):
        winner = player1
        player1.wins += 1
        player2.loses += 1
    # Player 2 wins
    elif (
        player2.id == 0 and player1.id == 1 or
        player2.id == 1 and player1.id == 2 or
        player2.id == 2 and player1.id == 0
        ):
        winner = player2
        player2.wins += 1
        player1.loses += 1
    # Tie
    else:
        player1.ties += 1
        player2.ties += 1
    
    return winner
    
    
    



main()





    




