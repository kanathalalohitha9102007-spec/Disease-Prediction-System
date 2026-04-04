import streamlit as st
import pickle
import numpy as np
import pandas as pd
from fpdf import FPDF

# -------------------------------
# PAGE CONFIG + UI STYLE
# -------------------------------
st.set_page_config(page_title="Disease Prediction System", layout="centered")

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD MODEL FILES
# -------------------------------
model = pickle.load(open("model.pkl", "rb"))
symptoms_list = pickle.load(open("symptoms.pkl", "rb"))

# -------------------------------
# TITLE + SIDEBAR
# -------------------------------
st.title("🏥 Disease Prediction System")
st.write("Select symptoms to predict possible disease")

st.sidebar.title("About")
st.sidebar.info("This app predicts diseases based on symptoms using Machine Learning.")

# -------------------------------
# SEARCH + SELECT SYMPTOMS
# -------------------------------
search = st.text_input("🔍 Search symptom")

filtered_symptoms = [s for s in symptoms_list if search.lower() in s.lower()]

selected_symptoms = st.multiselect("Select Symptoms:", filtered_symptoms)

# -------------------------------
# PREDICTION LOGIC
# -------------------------------
if st.button("Predict"):
    if len(selected_symptoms) == 0:
        st.warning("⚠️ Please select at least one symptom")
    else:
        input_data = [0] * len(symptoms_list)

        for symptom in selected_symptoms:
            index = symptoms_list.index(symptom)
            input_data[index] = 1

        input_data = np.array(input_data).reshape(1, -1)

        prediction = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0]

        # -------------------------------
        # RESULT DISPLAY
        # -------------------------------
        st.success(f"🩺 Predicted Disease: {prediction}")
        st.info(f"Confidence: {np.max(prob)*100:.2f}%")

        # -------------------------------
        # PROBABILITY CHART
        # -------------------------------
        df = pd.DataFrame({
            "Disease": model.classes_,
            "Probability": prob
        })

        st.subheader("📊 Prediction Probabilities")
        st.bar_chart(df.set_index("Disease"))

        # -------------------------------
        # SEVERITY MESSAGE
        # -------------------------------
        if prediction in ["Flu", "Cold"]:
            st.warning("⚠️ Mild condition. Take rest and drink fluids.")
            doctor = "General Physician"
        elif prediction == "Migraine":
            st.info("💡 Consult a doctor if symptoms persist.")
            doctor = "Neurologist"
        else:
            st.error("🚨 Serious condition. Seek medical attention immediately!")
            doctor = "Specialist"

        # -------------------------------
        # DOCTOR RECOMMENDATION
        # -------------------------------
        st.write(f"👨‍⚕️ Recommended Doctor: **{doctor}**")

        # -------------------------------
        # PDF DOWNLOAD
        # -------------------------------
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="Disease Prediction Report", ln=True)
        pdf.cell(200, 10, txt=f"Predicted Disease: {prediction}", ln=True)
        pdf.cell(200, 10, txt=f"Confidence: {np.max(prob)*100:.2f}%", ln=True)
        pdf.cell(200, 10, txt=f"Recommended Doctor: {doctor}", ln=True)

        pdf.output("report.pdf")

        with open("report.pdf", "rb") as file:
            st.download_button(
                label="📄 Download Report",
                data=file,
                file_name="disease_report.pdf",
                mime="application/pdf"
            )

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit + Machine Learning")