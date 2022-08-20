from IPython.display import clear_output

def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]}")

game_board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
display_board(game_board)


def player_input():
    p1_choice = ""
    p2_choice = ""
    print("Welcome to Tic Tac Toe!")
    while p1_choice not in ["x", "o"]:
        p1_choice = input("Player 1: Do you want to be x or o?: ").lower()
        
        if p1_choice not in ["x", "o"]:
            print("Sorry, please choose x or o.")
    if p1_choice == "x":
        p2_choice = "o"
        print("Player 1 is x and Player 2 is o. Player 1 will go first.")
    if p1_choice == "o":
        p2_choice = "x"
        print("Player 1 is o and player 2 is x.")
    
    return p1_choice, p2_choice
    
p1_choice, p2_choice = player_input()

def place_marker(board, marker, position):
    board[position-1] = marker

place_marker(game_board, "$", 8)

