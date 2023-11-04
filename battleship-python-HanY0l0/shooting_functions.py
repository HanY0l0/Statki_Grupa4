from board_functions import display_shooting_board
import os

def game_over(board, player):
    print(board)
    for row in board:
        for cell in row:
            if cell == "X":
                return False
    print(f"Congrats! Player: {player} won")
    exit()



def randomly_place_ships(board):
    # Place the player's ships randomly
    pass

def get_player_move(board, current_player):
        while True:
            coords = input(f"Player {current_player}, please provide shooting coordinates (row, column): ").upper()
            row = ord(coords[0]) - ord("A")
            col = int(coords[1]) - 1
            if len(coords) < 2 or len(coords) > 3 or coords[0] == " " or coords[1] == " " or not coords[0].isalpha() or not coords[1].isdigit():
                print("Wrong format, try again")
            elif row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                print("You're shooting outside the board, try again.")
            else:
                return row, col

def hit_or_miss(board, coordinates):
    row, col = coordinates
    if board[row][col] == "X":
        return "hit"
    elif board[row][col] == "0":
        return "miss"
    else:
        return False
    

def update_board(board, coordinates, result):
    row, col = coordinates
    if result == "hit":
        board[row][col] = "H"
    elif result == "miss":
        board[row][col] = "M"
    elif result == "sunk":
        board[row][col] = "S"
    return board


def play_battleship(player1, player2, player1_hidden_board, player2_hidden_board, player1_shooting_board, player2_shooting_board):
    for i in range(100):
        os.system('cls' if os.name == 'nt' else 'clear')
        current_player = player1 if i % 2 == 0 else player2
        current_shooting_board = player1_shooting_board if i % 2 == 0 else player2_shooting_board
        current_hidden_board = player2_hidden_board if i % 2 == 0 else player1_hidden_board
        display_shooting_board(current_shooting_board, current_player)
        coordinates = get_player_move(current_hidden_board, current_player)
        result = hit_or_miss(current_hidden_board, coordinates)
        update_board(current_shooting_board, coordinates, result)
        update_board(current_hidden_board, coordinates, result)
        display_shooting_board(current_shooting_board, current_player)
        input("Press Enter for next player's round...")
        if game_over(current_hidden_board, current_player):
            break