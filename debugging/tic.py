def print_board(board):
    """
    Prints the current state of the game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the current board state.

    Parameters:
        board (list): A 2D list representing the game board.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Checks if the board is full (no empty spaces).

    Parameters:
        board (list): A 2D list representing the game board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play a game of Tic-Tac-Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue
            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                if is_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                # Switch players
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")

tic_tac_toe()
