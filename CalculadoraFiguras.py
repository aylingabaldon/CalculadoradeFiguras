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
   r = st.number_input("Radio", min_value=0.0, value=1.0)
   area = np.pi * r**2        
   perimetro = 2 * np.pi * r
   st.write("Fórmula Área: A=C * r²")
   st.write("Fórmula Perímetro: P=2*π*r") 
elif figura == "Triángulo":
   a = st.number_input("Lado a", min_value=0.0, value=1.0) 
   b = st.number_input("Lado b (Base)", min_value=0.0, value=1.0)
   c = st.number_input("Lado c", min_value=0.0, value=1.0)
   h = st.number_input("Altura: ", min_value=0.0, value=1.0)
   area = (b * h) / 2
   perimetro = a + b + c
   st.write("Fórmula Área: (b * h)/2")
   st.write("Fórmula Perímetro: a + b + c")

elif figura == "Rectángulo":
    b = st.number_input("Base: ", min_value=0.0, value=1.0)
    h = st.number_input("Altura: ", min_value=0.0, value=2.0)
    area = b * h
    perimetro = 2 * (b + h)
    st.write("Fórmula Área: b * h")
    st.write("Fórmula Perímetro: 2 * (b + h)")

elif figura == "Cuadrado":
    l = st.number_input("Lado: ", min_value=0.0, value=1.0)
    area = l**2
    perimetro = 4 * l
    st.write("Fórmula Área: L * L")
    st.write("Fórmula Perímetro: 4*L")

st.success(f"Área = {area:.2f}")
st.success(f"Perímetro = {perimetro:.2f}")
   
    
  



