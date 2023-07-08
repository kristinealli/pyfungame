def create_board():
    board = [[' ' for _ in range(7)] for _ in range(6)]
    return board


def display_board(board):
    # Print the board to the console
    print('\n *CONNECT 4* ')
    for row in board:
        print('|'.join(row))
        print('-------------')
    print('1 2 3 4 5 6 7\n')


def make_move(board, column, player):
    # Update the board with the player's move
    # Find the first empty row in the selected column
    for row in range(5, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            break


def check_win(board, player):
    # Check rows for a winning combination
    for row in range(6):
        for col in range(4):
            if (
                board[row][col] == player and
                board[row][col+1] == player and
                board[row][col+2] == player and
                board[row][col+3] == player
            ):
                return True

    # Check columns for a winning combination
    for row in range(3):
        for col in range(7):
            if (
                board[row][col] == player and
                board[row+1][col] == player and
                board[row+2][col] == player and
                board[row+3][col] == player
            ):
                return True

    # Check diagonals (down-right) for a winning combination
    for row in range(3):
        for col in range(4):
            if (
                board[row][col] == player and
                board[row+1][col+1] == player and
                board[row+2][col+2] == player and
                board[row+3][col+3] == player
            ):
                return True

    # Check diagonals (up-right) for a winning combination
    for row in range(3, 6):
        for col in range(4):
            if (
                board[row][col] == player and
                board[row-1][col+1] == player and
                board[row-2][col+2] == player and
                board[row-3][col+3] == player
            ):
                return True

    return False


def check_draw(board):
    # Check if the game ends in a draw
    # If all spaces are filled and there is no winner, it's a draw
    for row in range(6):
        for col in range(7):
            if board[row][col] == ' ':
                return False
    return True


def play_game():
    board = create_board()

    # Get players' names
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    current_player = player1_name

    while True:
        display_board(board)
        column = -1

        # Prompt for a valid column input
        while column < 1 or column > 7 or board[0][column - 1] != ' ':
            column = int(
                input("{} enter your move (1-7): ".format(current_player)))
            if column < 1 or column > 7:
                print("Invalid move. Column must be between 1 and 7.")
            elif board[0][column - 1] != ' ':
                print("Invalid move. Column is already full.")

        # Find the first empty row in the selected column
        for row in range(5, -1, -1):
            if board[row][column - 1] == ' ':
                board[row][column - 1] = 'X' if current_player == player1_name else 'O'
                break

        if check_win(board, 'X'):
            display_board(board)
            print("{} wins!".format(player1_name))
            break
        elif check_win(board, 'O'):
            display_board(board)
            print("{} wins!".format(player2_name))
            break
        elif check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = player2_name if current_player == player1_name else player1_name

        # Validate if all columns are filled
        if all(board[row][col] != ' ' for col in range(7) for row in range(6)):
            display_board(board)
            print("All columns are filled. It's a draw!")
            break


# Start the game
play_game()
