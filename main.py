def print_board(board):
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("-----------")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("-----------")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True, board[i][0]
        elif board[0][i] == board[1][i] == board[2][i] != " ":
            return True, board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True, board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return True, board[0][2]
    elif " " not in [board[i][j] for i in range(3) for j in range(3)]:
        return True, "Tie"
    else:
        return False, ""

def play_game():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"
    print_board(board)
    while True:
        row = int(input("Player " + player + ", enter row (0-2): "))
        col = int(input("Player " + player + ", enter column (0-2): "))
        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue
        board[row][col] = player
        print_board(board)
        winner, winner_player = check_winner(board)
        if winner:
            if winner_player == "Tie":
                print("It's a tie!")
            else:
                print("Player " + winner_player + " wins!")
            break
        player = "O" if player == "X" else "X"

play_game()

