board =[
[".",".","."],
[".",".","."],
[".",".","."]]

# Global variables
winner = None
turn = "X"
plays = 0

# Introduction for User
print("Welcome to Tic Tac Toe!")
print("Rows go across → and columns go down ↓.")
print("Enter your moves as row, column.")
print("For example 0, 2 \n")
print("  0 1 2")
print("0 . . X  ← your X goes here")
print("1 . . .")
print("2 . . . \n")
print("Have fun!")

# Print Board
def print_board():
    print("\n  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))
    print()

def check_winner():
    # Check rows
    for row in board:
        if row[0] != "." and row.count(row[0]) == 3:
            return row[0]

    # Check columns
    for i in range(3):
        if board[0][i] != "." and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    # Check diagonals
    if board[0][0] != "." and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "." and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

# Runs while no one has won and there's no tie
while winner is None and plays < 9:
    print_board()
    play = input(f"Player {turn}, input your coordinates as row,col: ").replace(" ", "")

    #Process the input then check for errors
    try:
        row, col = play.split(",")
        row, col = int(row), int(col)

        #Error handling
        if row not in range(3) or col not in range(3):
            print("\nCoordinates must be 0, 1, or 2.\n")
            continue

        if board[row][col] != ".":
            print("\nYou've played here already, silly!\n")
            continue

    except (ValueError, IndexError):
        print("\nYour input was written incorrectly, whoops. Input is row, column (such as 0, 2)\n")
        continue


    board[row][col] = turn
    plays += 1

    winner = check_winner()
    if winner:
        print_board()
        print(f"Player {winner} won!")
        break

    turn = "O" if turn == "X" else "X"

if not winner:
    print_board()
    print("You tied. Play again soon!")
