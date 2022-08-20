import random

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def player_input():
    marker = ""
    while marker not in ["x", "o"]:
        marker = input("Player 1: Do you want to be x or o?: ").lower()

        if marker not in ["x", "o"]:
            print("Invalid input. Please choose x or o.")

    if marker == "x":
        print("Player 1 is x and Player 2 is o.")
        return ("x", "o")
    else:
        print("Player 1 is o and player 2 is x.")
        return ("o", "x")

def place_marker(board, marker, position):
    board[position-1] = marker

def win_check(board, mark):
    return ((board[6] == mark and board[7] == mark and board[8] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[0] == mark and board[1] == mark and board[2] == mark) or # across the bottom
    (board[6] == mark and board[3] == mark and board[0] == mark) or # down the middle
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the right side
    (board[6] == mark and board[4] == mark and board[2] == mark) or # diagonal
    (board[8] == mark and board[4] == mark and board[0] == mark)) # diagonal

def who_goes_first():
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"

def space_check(board, position):
    return board[position-1] == " "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = ""

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = input("Choose your next position (1-9): ")
        if position not in ["1","2","3","4","5","6","7","8","9"]:
            print("Invalid input. Please choose a position.")
        else:
            return position

def replay():
    play_again = ""

    while play_again not in ["y", "n"]:
        play_again = input("Do you still want to play? Enter y or n: ").lower()
        if play_again not in ["y", "n"]:
            print("Invalid input. Please enter y or n.")
    if play_again == "y":
        return True
    else:
        return False

print("Welcome to Tic Tac Toe")

while True:
    #sets up the tic tac toe board
    game_board = [" "] * 9

    #assign x and o to p1 and p2
    p1_marker, p2_marker = player_input()

    #randomly chooses who goes first
    turn = who_goes_first()
    print(f"{turn} will go first.")

    #check if player is ready
    play_game = ""
    while play_game not in ["y", "n"]:
        play_game = input("Are you ready to play? y or n: ").lower()

        if play_game not in ["y", "n"]:
            print("Invalid input. Please enter y or n.")

    if play_game == "y":
        game_on = True
    else:
        game_on = False
    
    #game continues to go on until a result is reached
    while game_on:
        if turn  == "Player 1":
            #p1's turn
            display_board(game_board)
            position = int(player_choice(game_board))
            place_marker(game_board, p1_marker, position)

            if win_check(game_board, p1_marker):
                display_board(game_board)
                print("Player 1 has won the game!")
                game_on = False
                break
            else:
                #check if the board is full without a clear winner
                if full_board_check(game_board):
                    display_board(game_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"
        else:
            #p2's turn
            display_board(game_board)
            position = int(player_choice(game_board))
            place_marker(game_board, p2_marker, position)

            if win_check(game_board, p2_marker):
                display_board(game_board)
                print("Player 2 has won the game!")
                game_on = False
                break
            else:
                #check if the board is full without a clear winner
                if full_board_check(game_board):
                    display_board(game_board)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 1"

    #if players choose not play again, the script stops
    if not replay():
        break