from board_functions import display_board

def are_ships_around(board, row, col):
    #Possible neigbouring positions
    neighbors = [(row - 1, col), (row + 1, col), (row, col -1), (row, col +1)]

    for neighbor_row, neighbor_col in neighbors:
        if 0 <= neighbor_row < len(board) and 0 <= neighbor_col < len(board[0]):
            if board[neighbor_row][neighbor_col] == "X":
                return True
    return False

def is_out_of_bounds(board, row, col):
    if row >= len(board) or col + 1 > len(board[0]):
        return True
    else:
        return False

def is_valid_coordinate(board, row, col):
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        if board[row][col] == '0':
            if are_ships_around(board, row, col):
                return False
            return True

    
def ask_for_starting_coordinate(board, current_player):
    while True:
        coords = input(f"Player {current_player}, please provide coordinates (row, column): ").upper()
        if len(coords) < 2 or len(coords) > 3 or coords[0] == " " or coords[1] == " " or not coords[0].isalpha() or not coords[1].isdigit():
            print("Wrong format, try again")
        else:    
            if len(coords) == 3:
                col = int(coords[1:]) - 1
            else:
                col = int(coords[1]) - 1
            
            row = ord(coords[0]) - ord("A")
            
            if is_out_of_bounds(board, row, col):
                print("Coordinate outside the board, try again")
            
            elif board[row][col] == "X":
                print("Already taken, try another one")
            
            elif is_valid_coordinate(board, row, col):
                return row, col
            
            else:
                print("Ships are too close, try again")


def place_ship(board, ships, current_player):
    directions = ["horizontal", "vertical", "h", "v"]
    list_ships = ships.items()
    for ship, ship_size in list_ships:
        print()
        print(f"Placing {ship} - {ship_size} spots")
        while True:
            display_board(board, current_player)
            start_coord = ask_for_starting_coordinate(board, current_player)
            direction = input("How do you want to place the ship (horizontal/vertical): ").lower()
            if direction not in directions:
                print("Command not recognized, try again")          
                continue
            if direction == "horizontal" or direction == "h":
                if start_coord[1] + ship_size > len(board[0]):
                    print("Ship is going overboard, try a different position")
                    continue
                for i in range(ship_size):
                    if are_ships_around(board, start_coord[0], start_coord[1] + i):
                        print("Ships touch or collide, try a different position")
                        break
                else:
                    for i in range(ship_size):
                        board[start_coord[0]][start_coord[1]+ i] = "X"
                    break
                
            if direction == "vertical" or direction == "v":
                if start_coord[0] + ship_size > len(board):
                    print("Ship is going overboard, try a different position")
                    continue
                for i in range(ship_size):
                    if are_ships_around(board, start_coord[0] + i, start_coord[1]):
                        print("Ships touch or collide, try a different position")
                        break
                else:
                    for i in range(ship_size):
                        board[start_coord[0]+ i][start_coord[1]] = "X"
                    break
            return board
        display_board(board, current_player)
    print("All ships are set")


