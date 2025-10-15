import streamlit as st
import math
st.title("Calculadora de Figuras Geométricas 💠")
figura = ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
figura_seleccionada = st.selectbox("Selecciona la figura", figura)
st.write("Figura: ", figura_seleccionada)

if figura == Círculo:
  operacion= ["Área", "Perímetro"]
  operacion_seleccionada = st.selectbox("Selecciona la operación", operacion)
  
