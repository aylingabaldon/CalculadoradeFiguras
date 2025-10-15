import streamlit as st
import math
st.title("Calculadora de Figuras Geométricas 💠")
figura = ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
figura_seleccionada = st.selecbox("Selecciona la figura", figura)
st.write("Figura: ", figura_seleccionada)
