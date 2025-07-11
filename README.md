# 🏨 Aplicación de Predicción de Cancelación de Reservas

Este proyecto es una aplicación desarrollada con **Streamlit** para predecir la probabilidad de que una reserva hotelera sea cancelada. El modelo fue entrenado con redes neuronales profundas usando Keras.

## 📦 Archivos del proyecto

- `app.py`: Script principal de la app con interfaz web en Streamlit.
- `modelo_entrenado.keras`: Modelo de red neuronal ya entrenado.
- `scaler.pkl`: Escalador `StandardScaler` usado para preprocesamiento.
- `requirements.txt`: Dependencias necesarias para ejecutar el proyecto.

## 🚀 Cómo usar esta aplicación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/JorgeJC84/cancelacion-reservas-app.git
   cd cancelacion-reservas-app

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt

streamlit run app.py

🔍 ¿Qué hace esta app?
Permite al usuario ingresar características básicas de una reserva (tiempo de antelación, cambios, solicitudes especiales, etc.), y predice si esa reserva probablemente será cancelada o no, mostrando un resultado visual.

📊 Modelo utilizado
Se utilizó una red neuronal multicapa con funciones de activación tanh, relu, sigmoid, entrenada con el optimizador RMSprop.
El modelo logró una precisión de validación del 77.34%.

📫 Autor
Desarrollado por Jorge Jeria Cortés, Ingeniero Civil Metalúrgico y futuro Científico de Datos.
