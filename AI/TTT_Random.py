import random

board = [" " for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("-----------")
    print("\n")

def check_winner(symbol):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  #rows
        [0,3,6], [1,4,7], [2,5,8],  #cols
        [0,4,8], [2,4,6]            #diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False

def is_full():
    return " " not in board

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    while True:
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != " ":
                    print("Invalid move, try again.")
                else:
                    board[move] = "X"
                    break
            except ValueError:
                print("Please enter a valid number (1-9).")

        print_board()
        if check_winner("X"):
            print("🎉 You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        print("Computer's turn...")
        while True:
            move = random.randint(0, 8)
            if board[move] == " ":
                board[move] = "O"
                break

        print_board()
        if check_winner("O"):
            print("💻 Computer wins!")
            break
        if is_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
