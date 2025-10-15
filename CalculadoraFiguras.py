import streamlit as st
import math
st.title("Calculadora de Figuras Geométricas 💠")
figura = ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
figura_seleccionada = st.selectbox("Selecciona la figura", figura)
st.write("Figura: ", figura_seleccionada)

def area_circulo(radio):
  return math.pi * radio ** 2
  radio = input("Ingresa el radio:")
  print(area_circulo(radio))
if figura == circulo:
  operacion= ["Área", "Perímetro"]
  operacion_seleccionada = st.selectbox("Selecciona la operación", operacion)
  
