import streamlit as st
import joblib

st.title("Demo ML CI/CD 🚀")

model = joblib.load("model.pkl")

x = st.number_input("Input nilai X:", value=1.0)
if st.button("Prediksi"):
    pred = model.predict([[x]])[0]
    st.success(f"Hasil prediksi: {pred:.2f}")
