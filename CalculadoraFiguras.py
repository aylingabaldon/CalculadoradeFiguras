import streamlit as st
import numpy as np
import matplotlib.pyplot as plt



st.title("Calculadora de Figuras Geométricas 💠")
st.sidebar.write("Nombre: Aylín Yareli Gabaldón Yáñez")
st.sidebar.write("Matrícula: 313765")
tabs = st.tabs(["Figuras Geométricas ❀", "Funciones Trigonométricas 〰️"])

# -----------------------------------------------------
# PARTE 1 y 2: FIGURAS GEOMÉTRICAS
# -----------------------------------------------------

with tabs[0]:
    st.header("Figuras Geométricas ❀")
    figura = st.selectbox(
        "Selecciona la figura:",
        ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
    )
    st.write("Figura: ", figura)
    color = st.color_picker("Selecciona un color: ", "#10B4E0")

    if figura == "Círculo":
        r = st.number_input("Radio: ", min_value=0.0, value=1.0)
        area = np.pi * r**2
        perimetro = 2 * np.pi * r
        st.latex("Fórmula Área: π * r²")
        st.metric("Área del Círculo: ", f"{area:.2f}")
        st.latex("Fórmula Perímetro: 2 * π * r")
        st.metric("Perímetro del Círculo: ", f"{perimetro:.2f}")

        fig, ax = plt.subplots()
        circulo = plt.Circle((0, 0), radio, color=color, fill=True)
        ax.add_artist(circulo)
        ax.set_aspect('equal')
        ax.set_xlim(-radio - 1, radio + 1)
        ax.set_ylim(-radio - 1, radio + 1)
        plt.title("Visualización del Círculo")
        st.pyplot(fig)

    elif figura == "Triángulo":
        a = st.number_input("Lado a", min_value=0.0, value=1.0)
        b = st.number_input("Lado b (base)", min_value=0.0, value=1.0)
        c = st.number_input("Lado c", min_value=0.0, value=1.0)
        h = st.number_input("Altura: ", min_value=0.0, value=1.0)
        area = 0.5 * b * h
        perimetro = a + b + c
        st.latex("Fórmula Área: (b * h) / 2")
        st.metric("Área del Tríangulo: ", f"{area:.2f}")
        st.latex("Fórmula Perímetro: a + b + c")
        st.metric("Perímetro del Triángulo: ", f"{perimetro:.2f}")
        
    elif figura == "Rectángulo":
        b = st.number_input("Base: ", min_value=0.0, value=1.0)
        h = st.number_input("Altura: ", min_value=0.0, value=1.0)
        area = b * h
        perimetro = 2 * (b + h)
        st.latex("Fórmula Área: b * h")
        st.metric("Área del Rectángulo: ", f"{area:.2f}")
        st.latex("Fórmula Perímetro: 2 * (b + h)")
        st.metric("Perímetro del Rectángulo: ", f"{perimetro:.2f}")
       

    elif figura == "Cuadrado":
        l = st.number_input("Lado: ", min_value=0.0, value=1.0)
        area = l**2
        perimetro = 4 * l
        st.latex("Fórmula Área: L * L")
        st.metric("Área del Cuadrado: ", f"{area:.2f}")
        st.latex("Fórmula Perímetro: 4 * L")
        st.metric("Perímetro del Cuadrado: ", f"{perimetro:.2f}")

# -----------------------------------------------------
# 🟦 PARTE 3: FUNCIONES TRIGONOMÉTRICAS
# -----------------------------------------------------
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


   
    
  



