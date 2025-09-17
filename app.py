import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Prediksi Harga Rumah - California Housing")

st.write("Masukkan nilai fitur berikut:")

# California housing punya 8 fitur
MedInc = st.number_input("Median Income (10k USD)", min_value=0.0, value=5.0, step=0.1)
HouseAge = st.number_input("House Age (tahun)", min_value=0.0, value=20.0, step=1.0)
AveRooms = st.number_input("Average Rooms", min_value=0.0, value=5.0, step=0.1)
AveBedrms = st.number_input("Average Bedrooms", min_value=0.0, value=1.0, step=0.1)
Population = st.number_input("Population", min_value=0.0, value=1000.0, step=10.0)
AveOccup = st.number_input("Average Occupancy", min_value=0.0, value=3.0, step=0.1)
Latitude = st.number_input("Latitude", min_value=32.0, max_value=42.0, value=34.0, step=0.1)
Longitude = st.number_input("Longitude", min_value=-124.0, max_value=-114.0, value=-118.0, step=0.1)

if st.button("Prediksi"):
    X_new = np.array([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
    pred = model.predict(X_new)
    st.success(f"Perkiraan harga rumah: {pred[0]:.2f} (dalam 100k USD)")
