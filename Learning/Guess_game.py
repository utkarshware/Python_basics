from IPython.display import clear_output

def display_game(game_list):
    print("Current game list:", game_list)

def position_choice():
    return int(input("Pick a position (0, 1, 2): "))

def replacement_choice(game_list, position):
    user_input = input("Enter a new value: ")
    game_list[position] = user_input
    return game_list

def gameon_choice():
    choice = input("Keep playing? (y/n): ").lower()
    return choice == 'y'

# Variable to keep game playing
game_on = True
game_list = [0, 1, 2]

while game_on:
    clear_output()
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list, position)
    clear_output()
    display_game(game_list)
    game_on = gameon_choice()
print("Thanks for playing!")