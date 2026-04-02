# app.py

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# -------------------------------
# TRAIN MODEL (inside app)
# -------------------------------
data = {
    "message": [
        "Win money now", "Free lottery", "Claim prize", "Urgent account update",
        "Congratulations you won", "Click here now",
        "Hello friend", "Let's meet tomorrow", "Call me later",
        "Are you coming to class", "See you soon", "Good morning"
    ],
    "label": [1,1,1,1,1,1, 0,0,0,0,0,0]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df["message"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="Spam Analyzer", layout="centered")

st.markdown("""
<style>
.main {
    background-color: #0f172a;
    color: white;
}
.stTextArea textarea {
    background-color: #1e293b;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("📩 AI-Powered Spam & Scam Message Analyzer")
st.write("Detect whether a message is **Spam/Scam or Safe** using Machine Learning.")

# Input
user_input = st.text_area("Enter your message:")

# Button
if st.button("Analyze Message"):

    if user_input.strip() == "":
        st.warning("Please enter a message!")
    else:
        input_data = vectorizer.transform([user_input])
        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.error("🚨 This message is likely SPAM / SCAM!")
        else:
            st.success("✅ This message is SAFE.")

# Footer
st.markdown("---")
st.caption("Developed using Streamlit + Machine Learning")