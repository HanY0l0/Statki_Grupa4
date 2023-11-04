def get_menu_option():
    while True:
        level = input(
            "Choose game mode:\n1. Human vs Human\n2. Human vs AI\n").lower()
        if level == "1" or level == "human vs human":
            return "human vs human"
            break
        elif level == "2" or level == "human vs ai":
            return "human vs ai"
            break
        if not level.isdigit():
            print("Wrong input, try again")
        else:
            print("Wrong choice, try again")

def get_player_names():
    player1 = input("Enter player 1 name: ")
    player2 = input("Enter player 2 name: ")
    
    while player1 == "" or player2 == "":
        print("Both names must be provided. Try again.")
        player1 = input("Enter player 1 name: ")
        player2 = input("Enter player 2 name: ")

    return player1, player2




