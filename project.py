import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
@st.cache_resource
def train_model():
    data = {
        "message": [
            "Win money now!!! Click here",
            "Congratulations you have won lottery",
            "Free entry in contest!!!",
            "Claim your prize now",
            "Urgent! Your account is hacked",
            "Call me later",
            "Hey how are you",
            "Let's meet tomorrow",
            "Are you coming to class?",
            "See you soon"
        ],
        "label": [1,1,1,1,1,0,0,0,0,0]  # 1 = Spam, 0 = Safe
    }

    df = pd.DataFrame(data)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df["message"])
    y = df["label"]

    model = MultinomialNB()
    model.fit(X, y)

    return model, vectorizer

model, vectorizer = train_model()
st.set_page_config(page_title="Spam Analyzer", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.big-title {
    text-align: center;
    font-size: 32px;
    color: #38bdf8;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">📩 AI-Powered Spam & Scam Message Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Detect Spam/Scam messages using Machine Learning</div>', unsafe_allow_html=True)

st.markdown("")
user_input = st.text_area("✉️ Enter your message here:", height=150)
if st.button("🔍 Analyze Message"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message!")
    else:
        input_data = vectorizer.transform([user_input])
        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0]
        confidence = max(prob) * 100
        st.markdown("---")
        if prediction == 1:
            st.error(f"🚨 SPAM / SCAM DETECTED!\nConfidence: {confidence:.2f}%")
        else:
            st.success(f"✅ SAFE MESSAGE\nConfidence: {confidence:.2f}%")
        spam_keywords = ["win", "free", "prize", "lottery", "urgent", "click"]
        found_words = [word for word in spam_keywords if word in user_input.lower()]
        if found_words:
            st.write("⚠️ Suspicious words detected:", ", ".join(found_words))
st.markdown("---")
st.caption("🚀 Built with Streamlit + Machine Learning | Mini Project")