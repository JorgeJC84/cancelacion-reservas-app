
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from keras.models import load_model

modelo = load_model("modelo_entrenado.keras")
escalador = joblib.load("scaler.pkl")

st.set_page_config(page_title="Predicción de Cancelación de Reserva", layout="centered")
st.title("🏨 Predicción de Cancelación de Reserva")

st.write("Ingrese los datos para predecir si la reserva será cancelada o no.")

lead_time = st.slider("Lead Time", 0, 500, 50)
booking_changes = st.slider("Cambios en la reserva", 0, 20, 1)
previous_cancellations = st.selectbox("Reservas canceladas antes", [0, 1, 2, 3])
total_of_special_requests = st.selectbox("Solicitudes especiales", [0, 1, 2, 3, 4, 5])
adr = st.number_input("ADR (€)", 0.0, 500.0, 100.0)

if st.button("🔍 Predecir cancelación"):
    entrada = pd.DataFrame({
        "lead_time": [lead_time],
        "booking_changes": [booking_changes],
        "previous_cancellations": [previous_cancellations],
        "total_of_special_requests": [total_of_special_requests],
        "adr": [adr]
    })
    entrada_escalada = escalador.transform(entrada)
    pred = modelo.predict(entrada_escalada)
    result = (pred > 0.5).astype(int)[0][0]
    if result == 1:
        st.error("❌ Probablemente será CANCELADA.")
    else:
        st.success("✅ Probablemente NO será cancelada.")
