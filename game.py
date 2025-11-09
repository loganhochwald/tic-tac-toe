import streamlit as st
from game_logic import init_game_state, make_move, reset_game

st.set_page_config(page_title="NOLA Tac Toe", page_icon="⚜️", layout="centered")

st.title("NOLA Tac Toe ⚜️")
st.markdown("Click a square to make your move!")

# Initialize session state
init_game_state()

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

# Restart
if st.button("Restart Game"):
    reset_game()
