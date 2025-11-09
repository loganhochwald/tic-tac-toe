import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", page_icon="⚜️", layout="centered")

st.title("NOLA Tac Toe ⚜️")
st.markdown("Click a square to make your move!")

# Initialize session state (global variables)
if "board" not in st.session_state:
    st.session_state.board = [[".",".","."],[".",".","."],[".",".","."]]
if "winner" not in st.session_state:
    st.session_state.winner = None
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "plays" not in st.session_state:
    st.session_state.plays = 0

# Check for a winner
def check_winner():
    board = st.session_state.board

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

# Handle a move
def make_move(row, col):
    # If there's already a winner or the cell is occupied, do nothing
    if st.session_state.winner or st.session_state.board[row][col] != ".":
        return

    # Make the move
    st.session_state.board[row][col] = st.session_state.turn
    st.session_state.plays += 1

    # Check for a winner
    winner = check_winner()
    if winner:
        st.session_state.winner = winner
    elif st.session_state.plays == 9:
        st.session_state.winner = "Tie"
    else:
        st.session_state.turn = "O" if st.session_state.turn == "X" else "X"


# Draw the board with streamlit buttons
for row in range(3):
    columns = st.columns(3)
    for col in range(3):
        value = st.session_state.board[row][col]
        text = " " if value == "." else value
        columns[col].button(text, key=f"{row}-{col}", on_click=make_move, args=(row, col), use_container_width=True)


# Results
if st.session_state.winner == "Tie":
    st.info("You tied. Play again soon!")
elif st.session_state.winner:
    st.success(f"Player {st.session_state.winner} won!")
else:
    st.write(f"Player {st.session_state.turn}'s turn")

# ---- Restart ----
if st.button("Restart Game"):
    st.session_state.board = [["."] * 3 for _ in range(3)]
    st.session_state.turn = "X"
    st.session_state.winner = None
    st.session_state.plays = 0
