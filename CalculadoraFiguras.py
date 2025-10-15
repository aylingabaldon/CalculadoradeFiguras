import streamlit as st
import math
st.title("Calculadora de Figuras Geométricas 💠")
st.sidebar.write("Nombre: Aylín Yareli Gabaldón Yáñez")
st.sidebar.write("Matrícula: 313765")
figura = ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
figura_seleccionada = st.selectbox("Selecciona la figura", figura)
st.write("Figura: ", figura_seleccionada)

if figura == Círculo:
 st.latex("A=π * r²")
 st.number_input("Radio")
def area_circulo(radio):
  return math.pi * radio ** 2
print(st.success(area_circulo))


