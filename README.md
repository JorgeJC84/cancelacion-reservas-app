---
title: Cancelación de Reservas App
emoji: 🔔
colorFrom: indigo
colorTo: blue
sdk: gradio
sdk_version: 4.27.0
app_file: app.py
pinned: false
license: mit
---

# 🔔 Cancelación de Reservas App

Esta aplicación predice si una reserva será **cancelada o no** en función de variables como:

- Lead Time
- Cambios en la reserva
- Reservas canceladas previamente
- Solicitudes especiales
- ADR (€ por noche)

El modelo ha sido entrenado con redes neuronales utilizando TensorFlow/Keras y se despliega con **Gradio** en Hugging Face Spaces.

## 🛠 Archivos principales

- `app.py`: código principal de la app con interfaz Gradio
- `modelo_entrenado.keras`: modelo de predicción entrenado
- `scaler.pkl`: transformador para escalar los datos antes de la predicción
- `requirements.txt`: dependencias necesarias

## 🚀 ¿Cómo usar la app?

1. Ajusta los valores con los controles de la izquierda.
2. Haz clic en **Submit**.
3. Verás la predicción a la derecha.

> ✅ `Probablemente NO será cancelada.`  
> ❌ `Probablemente será CANCELADA.`

---

¡Gracias por visitar esta app! Construida con 💡 y desplegada en Hugging Face Spaces.
