import streamlit as st
import requests
st.title("Joke App")
if st.button("Get Random Joke"):
    url="https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    data = response.json()
    st.write(f"{data['setup']}