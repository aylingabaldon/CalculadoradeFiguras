import streamlit as st
import math
st.title("Calculadora de Figuras Geométricas 💠")
st.sidebar.write("Nombre: Aylín Yareli Gabaldón Yáñez")
st.sidebar.write("Matrícula: 313765")
figura = ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
figura_seleccionada = st.selectbox("Selecciona la figura", figura)
st.write("Figura: ", figura_seleccionada)

st.latex("A=π * r²")

def area_circulo(radio):
  return math.pi * radio ** 2
st.number_input("Radio")
st.success(area_circulo(radio))
