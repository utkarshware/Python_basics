import random
import os

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    marker = ''
    while marker not in ['X', 'O']:
        marker = input("Choose your marker (X or O): ").upper()
    return (marker, 'O' if marker == 'X' else 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))

def choose_first():
    return random.choice(['Player', 'Computer'])

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return all(board[i] != ' ' for i in range(1, 10))

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        try:
            position = int(input("Choose your position (1-9): "))
        except ValueError:
            print("Enter a number between 1 and 9.")
    return position

def computer_choice(board):
    available = [i for i in range(1, 10) if space_check(board, i)]
    return random.choice(available)

def replay():
    return input('Play again? (Yes/No): ').lower().startswith('y')

print("Welcome to Tic Tac Toe!")

while True:
    theBoard = [' '] * 10
    player_marker, computer_marker = player_input()
    turn = choose_first()
    print(turn + " will go first.")
    game_on = input("Ready to play? (Yes/No): ").lower().startswith('y')

    while game_on:
        if turn == 'Player':
            display_board(theBoard)
            pos = player_choice(theBoard)
            place_marker(theBoard, player_marker, pos)

            if win_check(theBoard, player_marker):
                display_board(theBoard)
                print("You have won!")
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print("It's a draw!")
                break
            else:
                turn = 'Computer'

        else:  
            pos = computer_choice(theBoard)
            place_marker(theBoard, computer_marker, pos)
            display_board(theBoard)  

            if win_check(theBoard, computer_marker):
                print("Computer has won!")
                game_on = False
            elif full_board_check(theBoard):
                print("It's a draw!")
                break
            else:
                turn = 'Player'

    if not replay():
        break
