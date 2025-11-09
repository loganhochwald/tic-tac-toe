import streamlit as st

emoji_choices = ["🎭", "🎺", "🍹", "⚜️"]

# Show dialogue for emoji selection
@st.dialog("Players, Choose your Game Emojis!", dismissible=False)
def choose_emojis():
    # Layout two columns for selection
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.player_x = st.selectbox(
            "Player 1 Emoji",
            emoji_choices,
            key="x",
            index=emoji_choices.index(st.session_state["player_x"])
        )
    with col2:
        st.session_state.player_o = st.selectbox(
            "Player 2 Emoji",
            emoji_choices,
            key="o",
            index=emoji_choices.index(st.session_state["player_o"])
        )

    # Only show the Submit button if emojis are different
    if st.session_state.player_x == st.session_state.player_o:
        st.warning("Players must choose different emojis!")
    else:
        if st.button("Submit"):
            st.session_state.emojis_selected = True
            st.success("Emojis selected!")
            st.rerun()
