import streamlit as st
import math
st.title("Calculadora de Figuras Geométricas 💠")
figura = ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
figura_seleccionada = st.selectbox("Selecciona la figura", figura)
st.write("Figura: ", figura_seleccionada)

st.latex("A=π * r²")
![](https://www.google.com/url?sa=i&url=https%3A%2F%2Fillustoon.com%2Fes%2F%3Fid%3D7441&psig=AOvVaw2yH-3Rqv-4NGA4GA1ZWr87&ust=1760628594770000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCPipouLCppADFQAAAAAdAAAAABAE)

def area_circulo(radio):
  return math.pi * radio ** 2
st.number_input("Radio")
