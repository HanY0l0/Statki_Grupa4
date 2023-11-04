from start_game_functions import get_menu_option, get_player_names
from coordinates import place_ship
from board_functions import ask_for_board_size, create_empty_board, display_board
from shooting_functions import play_battleship, game_over
def main():
    game_mode = get_menu_option()
    grid = ask_for_board_size()
    player1_hidden_board = create_empty_board(grid)
    player2_hidden_board = create_empty_board(grid)
    player1_shooting_board = create_empty_board(grid)
    player2_shooting_board = create_empty_board(grid)

    if game_mode == "human vs human" and grid == 5:
        ships = {"DESTROYER": 2, "GUNBOAT": 1}
        player1, player2 = get_player_names()
        print()
        place_ship(player1_hidden_board, ships, player1)
        input(f"{player2}, press Enter when ready to place your ships...")
        place_ship(player2_hidden_board, ships, player2)
        print()
        input(f"{player1, player2}, press Enter when ready to play...")
        play_battleship(player1, player2, player1_hidden_board, player2_hidden_board, player1_shooting_board, player2_shooting_board)

    if game_mode == "human vs human" and grid == 10:
        ships = {"CARRIER": 5, "BATTLESHIP": 4, "CRUISER": 3, "SUBMARINE": 3, "DESTROYER": 2}
        player1, player2 = get_player_names()
        print()
        place_ship(player1_hidden_board, ships, player1)
        input(f"{player2}, press Enter when ready to place your ships...")
        place_ship(player2_hidden_board, ships, player2)

if __name__ == "__main__":
    main()
