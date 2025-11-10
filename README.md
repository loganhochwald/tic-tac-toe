# NOLA-Tac-Toe ⚜️

A fun, interactive tic-tac-toe game built with **Streamlit** that lets players choose emojis as their game pieces. The game is NOLA-themed and emphasizes a playful, visual experience.

[nola-tac-toe.streamlit.app](https://nola-tac-toe.streamlit.app/)

*Note: It currently only works on the web, there was not enough time to diagnose the layout issue for mobile.*

## Features Implemented

### Game Mechanics
- Classic **3x3 Tic-Tac-Toe** board.
- Players take turns placing their chosen emoji on the board.
- Automatic **win detection** for rows, columns, and diagonals.
- Detects **tie games** when the board is full.
- Supports **game restart** at any time, with a **confirmation dialog**.
- **Move history tracking**: records each move with player emoji and coordinates.

### Emoji Selection
- Players can **select custom emojis** as their X and O pieces.
- Includes a **dialog box for emoji selection**.
- Ensures players **cannot select the same emoji**.
- Option to **change emojis** during gameplay.

### User Interface
- Fully implemented in **Streamlit** with a responsive layout.
- Dynamic buttons for each cell showing the chosen emoji.
- Displays **current player’s turn**.
- Shows **winner or tie** message once the game ends.
- **Move history displayed visually** using Streamlit containers and columns.
- Supports **custom text colors** and styling via `config.toml`.

### Session State Management
- Uses `st.session_state` to track:
  - Game board state.
  - Winner.
  - Current Turn.
  - Number of plays.
  - Selected emojis.
  - Move history.

### NOLA Theme
- Incorporates emojis like `⚜️`, `🎭`, `🎺`, and `🍹` to reflect New Orleans culture.
- Clean, centered layout suitable for desktop screens.


## How to Run

1. Install Streamlit using `pip install streamlit`.

2. Run the app with `streamlit run app.py`.

3. Open the provided local URL in your browser.
