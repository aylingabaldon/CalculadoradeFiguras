import streamlit as st
import numpy as np

st.title("Calculadora de Figuras Geométricas 💠")
st.sidebar.write("Nombre: Aylín Yareli Gabaldón Yáñez")
st.sidebar.write("Matrícula: 313765")
tabs = st.tabs(["Figuras Geométricas ❀", "Funciones Trigonométricas 〰️"])

with tabs[0]:
   st.header("Figuras Geométricas ❀")
   figura = ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
   figura_seleccionada = st.selectbox("Selecciona la figura", figura)
   st.write("Figura: ", figura_seleccionada)
   color = st.color_picker("Selecciona un color: ", "#10B4E0")

if figura == "Círculo":
   r = st.number_input("Radio", min_value=0.0, value=1)
   area =("Área: ", "np.pi * r**2")
   formula =("Fórmula: ", st.latex("A=π * r²"))
   perimetro =("Perimetro: ", "2 * np.pi * r")
  



