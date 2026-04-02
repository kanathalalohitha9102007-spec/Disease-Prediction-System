import streamlit as st
import pickle
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.set_page_config(page_title="Spam & Scam Analyzer", layout="centered")

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

user_input = st.text_area("Enter your message:")

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
st.markdown("---")
st.caption("Developed using Streamlit + Machine Learning")