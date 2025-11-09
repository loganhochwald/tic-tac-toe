import streamlit as st
from game_logic import init_game_state, make_move, reset_game
from emoji_selector import choose_emojis


st.set_page_config(page_title="NOLA Tac Toe", page_icon="⚜️", layout="centered")

st.title("NOLA Tac Toe ⚜️")

# Initialize session state
init_game_state()

# Emoji selection
if not st.session_state.get("emojis_selected", False):
    choose_emojis()

player_x = st.session_state.player_x
player_o = st.session_state.player_o

# Results
if st.session_state.winner == "Tie":
    st.info("You tied. Restart Game?")
elif st.session_state.winner == "X":
    st.success(f"{player_x} won!")
elif st.session_state.winner == "O":
    st.success(f"{player_o} won!")
else:
    if st.session_state["emojis_selected"]:
        current_turn = player_x if st.session_state.turn == "X" else player_o
        st.write(f"{current_turn}'s turn")

# Draw the board with streamlit buttons and emojis
if player_x != player_o:
    for row in range(3):
        columns = st.columns(3)
        for col in range(3):
            value = st.session_state.board[row][col]
            if value == ".":
                text = " "
            elif value == "X":
                text = player_x
            elif value == "O":
                text = player_o
            else:
                text = value
            
            columns[col].button(text, key=f"{row}-{col}", on_click=make_move, args=(row, col), use_container_width=True)

# Add spacing between board and control buttons
st.write("")
st.write("")

col1, col2 = st.columns(2)

with col1:
    if st.button("Change Emoji", use_container_width=True):
        st.session_state.emojis_selected = False
        choose_emojis()

with col2:
    if st.button("Restart Game", use_container_width=True):
        reset_game()
