def ask_for_board_size():
    user_board_size = int(input("Enter the size of the board (5/10): "))
    while user_board_size != 10 and user_board_size != 5:
        print("Invalid input! (must be 5 or 10)")
        user_board_size = int(input("Enter the size of the board: "))
    return user_board_size

def create_empty_board(board_size):
    return [['0' for i in range(board_size)] for i in range(board_size)]

def display_board(board, current_player):
    print("-------------------------------")
    print(f"PLACING FOR PLAYER:  {current_player}   ")
    print("______________________________")
    print("\x1b[34m    ", end="")

    for column in range(1, len(board) + 1):
        print(f"\x1b[31m{column}\x1b[0m  ", end=" ")

    print()

    for i, row in enumerate(board):
        print(f"\x1b[34m{chr(65 + i)}\x1b[0m  ", end="")

        for cell in row:
            print(f" {cell} |", end="")

        print('\n    ' + '--- ' * len(board))

def display_shooting_board(board, current_player):
    print("-------------------------------")
    print(f"PLAYER: {current_player} SHOOTING BOARD   ")
    print("______________________________")
    print("\x1b[34m    ", end="")

    for column in range(1, len(board) + 1):
        print(f"\x1b[31m{column}\x1b[0m  ", end=" ")

    print()

    for i, row in enumerate(board):
        print(f"\x1b[34m{chr(65 + i)}\x1b[0m  ", end="")

        for cell in row:
            print(f" {cell} |", end="")

        print('\n    ' + '--- ' * len(board))