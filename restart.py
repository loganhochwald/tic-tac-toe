import streamlit as st
from game_logic import reset_game

@st.dialog("Confirm Restart?", dismissible=True)
def confirm_restart():
    st.warning("Are you sure you want to restart the game?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes, Restart", use_container_width=True):
            reset_game()
            st.success("Game restarted!")
            st.rerun()
    
    with col2:
        if st.button("Cancel", use_container_width=True):
            st.info("Restart cancelled.")
            st.rerun()
