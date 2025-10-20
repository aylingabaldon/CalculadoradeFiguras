import streamlit as st
import numpy as np

st.title("Calculadora de Figuras Geométricas 💠")
st.sidebar.write("Nombre: Aylín Yareli Gabaldón Yáñez")
st.sidebar.write("Matrícula: 313765")
tabs = st.tabs("Figuras Geométricas ❀", "Funciones Trigonométricas 〰️")

with tab[0]:
   st.header("Figuras Geométricas ❀")
   figura = ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
   figura_seleccionada = st.selectbox("Selecciona la figura", figura)
   st.write("Figura: ", figura_seleccionada)
   color = st.color_picker("Selecciona un color: ", "#1f77b4")

if figura == "Círculo":
   print("Fórmula: ", st.latex("A=π * r²"))
   r = st.number_input("Radio")
   area = np.pi * r**2
   print("Área: ", area)
   perimetro = 2 * np.pi * r
   print("Perímetro: ", perimtro)



