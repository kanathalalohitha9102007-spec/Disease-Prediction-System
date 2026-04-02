import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
st.set_page_config(page_title="HIRING!!!")
st.title("Employee Hiring Prediction!!!")
data = {
    "Experience": [1,2,3,4,5],
    "TestScore": [50,60,70,80,90],
    "Communication":[5,6,7,8,9],
    "Hired":[0,0,1,1,1]
}
df=pd.DataFrame(data)
X=df[["Experience","TestScore","Communication"]]
y=df["Hired"]
model = RandomForestClassifier()
model.fit(X,y)

st.sidebar.header("Enter Candidate Details")
experience = st.sidebar.slider("Years of Experience", 0, 10, 1)
test_score = st.sidebar.slider("Test Score", 0, 100, 60)
communication = st.sidebar.slider("Communication Skills (1-10)", 1, 10, 5)
if st.sidebar.button("Predict Hiring"):
    prediction = model.predict([[experience, test_score, communication]])
    if prediction[0] == 1:
        st.success("The candidate is likely to be hired!")
    else:
        st.error("The candidate is unlikely to be hired.")