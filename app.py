import streamlit as st
import random
st.set_page_config(page_title="Guess Me Game",page_icon=":game_die:",layout="centered")
st.title("🎮 Welcome to the Guess Me Game!")
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
max_attempts = 5
guess=st.number_input("Enter your guess (1-100):", 
                      min_value=1, max_value=100, step=1)
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess< st.session_state.number:
       st.warning("Guess Higher!!!")
    elif guess > st.session_state.number:
        st.warning("Guess Lower!!!")
    else:
        st.success(f"Congratulations! You've guessed the number {st.session_state.number} in {st.session_state.attempts} attempts!")
        st.balloons()
    if st.session_state.attempts >= max_attempts and guess != st.session_state.number:
        st.error(f"Game Over! You've used all {max_attempts} attempts. The correct number was {st.session_state.number}.")
    st.write(f"Attempts left:{max_attempts -st.session_state.attempts}")
if st.button("Restart Game"):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.success("Game Restarted! Try to guess the new number.")
    