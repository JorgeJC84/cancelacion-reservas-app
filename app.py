import gradio as gr
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
import joblib

# Cargar modelo y escalador
modelo = load_model("modelo_entrenado.keras")
escalador = joblib.load("scaler.pkl")

# Lista de columnas en el orden correcto
columnas = ['lead_time', 'booking_changes', 'previous_cancellations',
            'total_of_special_requests', 'is_repeated_guest', 'adr']

# Función de predicción
def predecir_cancelacion(lead_time, booking_changes, previous_cancellations,
                          special_requests, adr, is_repeated_guest):
    try:
        entrada = pd.DataFrame([[lead_time, booking_changes, previous_cancellations,
                                 special_requests, int(is_repeated_guest), adr]],
                               columns=columnas)

        entrada_escalada = escalador.transform(entrada)
        prediccion = modelo.predict(entrada_escalada)[0][0]
        resultado = "❌ Cancelará" if prediccion >= 0.5 else "✅ No cancelará"
        color = "🔴" if prediccion >= 0.5 else "🟢"
        return f"🔎 Probabilidad: {prediccion:.2%}", f"{color} {resultado}"
    except Exception as e:
        return f"Error: {str(e)}", "❌ Error en la predicción"

# Interfaz Gradio
with gr.Blocks(theme=gr.themes.Soft(), title="Cancelación de Reservas") as interfaz:
    gr.Markdown("## 🛎️ Predicción de Cancelación de Reserva")
    gr.Markdown("Ingresa los datos de la reserva para predecir si será cancelada o no.")

    with gr.Row():
        with gr.Column():
            lead_time = gr.Slider(0, 500, value=100, label="Lead Time")
            booking_changes = gr.Slider(0, 20, step=1, value=1, label="Cambios en la reserva")
            previous_cancellations = gr.Dropdown([0, 1, 2, 3, 4], value=0, label="Reservas canceladas antes")
            special_requests = gr.Dropdown([0, 1, 2, 3, 4, 5], value=0, label="Solicitudes especiales")
            adr = gr.Slider(0, 500, value=100, label="ADR (€/noche)")
            is_repeated_guest = gr.Checkbox(label="¿Cliente repetido?", value=False)
            boton_clear = gr.Button("Clear")
            boton_predecir = gr.Button("Submit", variant="primary")

        with gr.Column():
            salida_texto = gr.Textbox(label="Resultado de la predicción")
            salida_color = gr.Textbox(label="Indicador tipo semáforo")

    # Conexión del botón Submit
    boton_predecir.click(
        predecir_cancelacion,
        inputs=[lead_time, booking_changes, previous_cancellations, special_requests, adr, is_repeated_guest],
        outputs=[salida_texto, salida_color]
    )

    # Conexión del botón Clear
    boton_clear.click(
        lambda: [100, 1, 0, 0, 100, False, "", ""],
        outputs=[lead_time, booking_changes, previous_cancellations, special_requests, adr, is_repeated_guest, salida_texto, salida_color]
    )

# Lanzar la app
interfaz.launch()
