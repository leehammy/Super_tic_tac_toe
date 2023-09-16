import numpy as np

def create_board():
    return np.full((9, 9), " ")

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(9):
        if (board[i] == player).all() or (board[:, i] == player).all():
            return True
    if (np.diag(board) == player).all() or (np.diag(np.fliplr(board)) == player).all():
        return True
    return False

def mini_toe(board, mini_board, player, row, col):
    if mini_board[row][col] == " ":
        mini_board[row][col] = player
        if check_winner(mini_board, player):
            board[row // 3][col // 3] = player

def main():
    tic_tac_toe_board = create_board()
    mini_boards = [create_board() for _ in range(9)]
    current_player = "X"

    while True:
        print_board(tic_tac_toe_board)
        print(f"Player {current_player}'s turn.")

        while True:
            try:
                mini_board_idx = int(input("Choose a mini board (0-8): "))
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if 0 <= mini_board_idx < 9 and 0 <= row < 3 and 0 <= col < 3:
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        mini_toe(tic_tac_toe_board, mini_boards[mini_board_idx], current_player, row, col)

        if check_winner(tic_tac_toe_board, current_player):
            print_board(tic_tac_toe_board)
            print(f"Player {current_player} wins!")
            break

        current_player = "X" if current_player == "O" else "O"

if __name__ == "__main__":
    main()
