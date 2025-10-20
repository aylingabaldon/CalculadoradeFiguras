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
        r = st.number_input("Radio: ", min_value=0.0, value=1.0)
        area = np.pi * r**2
        perimetro = 2 * np.pi * r

    elif figura == "Triángulo":
        a = st.number_input("Lado a", min_value=0.0, value=1.0)
        b = st.number_input("Lado b (base)", min_value=0.0, value=2.0)
        c = st.number_input("Lado c", min_value=0.0, value=3.0)
        h = st.number_input("Altura (h)", min_value=0.0, value=4.0)
        area = 0.5 * b * h
        perimetro = a + b + c

    elif figura == "Rectángulo":
        b = st.number_input("Base: ", min_value=0.0, value=4.0)
        h = st.number_input("Altura: ", min_value=0.0, value=2.0)
        area = b * h
        perimetro = 2 * (b + h)

    elif figura == "Cuadrado":
        l = st.number_input("Lado (l)", min_value=0.0, value=2.0)
        area = l**2
        perimetro = 4 * l

    st.success(f"Área = {area:.2f}")
    st.success(f"Perímetro = {perimetro:.2f}")

with tabs[1]:
    st.header("Funciones trigonométricas")

    # Selección de función
    funcion = st.selectbox("Selecciona una función:", ["sin(x)", "cos(x)", "tan(x)"])
    amp = st.slider("Amplitud", 0.1, 2.0, 1.0)
    rango = st.slider("Rango (en múltiplos de π)", 1, 4, 2)

    # Crear eje x
    x = np.linspace(0, rango * np.pi, 400)

    # Evaluar función seleccionada
    if funcion == "sin(x)":
        y = amp * np.sin(x)
    elif funcion == "cos(x)":
        y = amp * np.cos(x)
    else:
        y = amp * np.tan(x)
        y[np.abs(y) > 10] = np.nan  # limitar valores grandes


with tabs[0]:
   st.header
   
   
   
   

if figura == "Círculo":
  r = st.number_input("Radio", min_value=0.0, value=1.0)
  st.write("Fórmula Área: A=C * r²")
  area = np.pi * r**2
  print("Área: ", area)
  st.write("Fórmula Perímetro: P=2*π*r")
  perimetro = 2 * np.pi * r
  print("Perímetro: ", perimetro)

elif figura == "Triángulo":
  a = st.number_input("Lado a", min_value=0.0, value=1.0)
  b = st.number_input("Lado b (Base)", min_value=0.0, value=1.0)
  c = st.number_input("Lado c", min_value=0.0, value=1.0)
  h = st.number_input("Altura: ", min_value=0.0, value=1.0)
  st.write("Fórmula Área: (b * h)/2")
  area = (b * h) / 2
  print("Área: ", area)
  st.write("Fórmula Perímetro: a + b + c")
  perimetro = a + b + c
  print("Perímetro: ", perimetro)

elif figura == "Rectángulo":
  b = st.number_input("Base: ", min_value=0.0, value=1.0)
  h = st.number_input("Altura: ", min_value=0.0, value=2.0)
  st.write("Fórmula Área: b * h")
  area = b * h
  print("Área: ", area)
  st.write("Fórmula Perímetro: 2 * (b + h)") 
  perimetro = 2 * (b + h)
  print("Perímetro: ", perimetro)

elif figura == "Cuadrado":
  l = st.number_input("Lado: ", min_value=0.0, value=1.0)
  t.write("Fórmula Área: L * L")
  area = l**2
  print("Área: ", area)
  perimetro = 4 * l
  st.write("Fórmula Perímetro: 4*L")
  print("Perímetro: ", perimetro)

st.success(f"Área = {area:.2f}")
st.success(f"Perímetro = {perimetro:.2f}")


   
    
  



