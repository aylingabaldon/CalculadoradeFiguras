import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import math



st.title("Calculadora de Figuras Geométricas 💠")
st.sidebar.write("Nombre: Aylín Yareli Gabaldón Yáñez")
st.sidebar.write("Matrícula: 313765")
st.sidebar.write("Materia: Programación")
St.sidebar.write("Grupo: 3L")
tabs = st.tabs(["Figuras Geométricas ❀", "Funciones Trigonométricas 〰️", "Otras Funciones 😎"])

with tabs[0]:
    st.header("Figuras Geométricas ❀")
    figura = st.selectbox(
        "Selecciona la figura:",
        ["Círculo", "Triángulo", "Rectángulo", "Cuadrado"]
    )
    st.write("Figura: ", figura)
    color = st.color_picker("Selecciona un color: ", "#10B4E0")

    if figura == "Círculo":
        radio = st.number_input("Radio: ", min_value=0.0, value=1.0)
        area = np.pi * radio**2
        perimetro = 2 * np.pi * radio
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
        plt.title("Gráfica del Círculo")
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
        
        fig_t, ax_t = plt.subplots()
        x = [-b, b, 0]
        y = [0, 0, h]
        triangulo = plt.Polygon(list(zip(x, y)), color=color, fill=True)
        ax_t.add_patch(triangulo)
        ax_t.set_xlim(-b, b)
        ax_t.set_ylim(0, h + 2)
        ax_t.set_aspect('equal')
        ax_t.axis('on')
        plt.title("Gráfica del Triángulo")
        st.pyplot(fig_t)


        
    elif figura == "Rectángulo":
        b = st.number_input("Base: ", min_value=0.0, value=1.0)
        h = st.number_input("Altura: ", min_value=0.0, value=1.0)
        area = b * h
        perimetro = 2 * (b + h)
        st.latex("Fórmula Área: b * h")
        st.metric("Área del Rectángulo: ", f"{area:.2f}")
        st.latex("Fórmula Perímetro: 2 * (b + h)")
        st.metric("Perímetro del Rectángulo: ", f"{perimetro:.2f}")
        
        fig_rec, ax_rec = plt.subplots()
        rec = plt.Rectangle((0, 0), b, h, color=color, fill=True)
        ax_rec.add_patch(rec)
        ax_rec.set_xlim(-1, b + 1)
        ax_rec.set_ylim(-1, h + 1)
        ax_rec.set_aspect('equal')
        ax_rec.axis('on')
        plt.title("Gráfica del Rectángulo")
        st.pyplot(fig_rec)

    elif figura == "Cuadrado":
        l = st.number_input("Lado: ", min_value=0.0, value=1.0)
        area = l**2
        perimetro = 4 * l
        st.latex("Fórmula Área: L * L")
        st.metric("Área del Cuadrado: ", f"{area:.2f}")
        st.latex("Fórmula Perímetro: 4 * L")
        st.metric("Perímetro del Cuadrado: ", f"{perimetro:.2f}")

        fig_cuadro, ax_cuadro = plt.subplots()
        cuadrado = plt.Rectangle((0, 0), l, l, color=color, fill=True)
        ax_cuadro.add_patch(cuadrado)
        ax_cuadro.set_xlim(-1, l + 1)
        ax_cuadro.set_ylim(-1, l + 1)
        ax_cuadro.set_aspect('equal')
        ax_cuadro.axis('on')
        plt.title("Gráfica del Cuadrado")
        st.pyplot(fig_cuadro)

with tabs[1]:
    st.header("Funciones Trigonométricas 〰️")
    funcion = st.selectbox("Selecciona la función:", ["Seno", "Coseno", "Tangente"])
    frecuencia = st.slider("Frecuencia", 0.1, 15.0, 1.0)
    amplitud = st.slider("Amplitud", 0.1, 15.0, 1.0)
    x = np.linspace(0, 15, 600)

    if funcion == "Seno":
        y = amplitud * np.sin(frecuencia * x)
    elif funcion == "Coseno":
        y = amplitud * np.cos(frecuencia * x)
    elif funcion == "Tangente":
        y = amplitud * np.tan(frecuencia * x)
        y[np.abs(y) > 10] = np.nan
    
        fig_funTri, ax_funTri = plt.subplots()
        ax_funTri.plot(x, y, color=color)
        ax_funTri.set_title(f"Gráfica de la función: {funcion}")
        ax_funTri.grid(True)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        st.pyplot(fig_funTri)  
    
with tabs[2]:
    st.header("Otras Funciones 😎")
    funciones = st.selectbox("Selecciona la función:", ["Fórmula General🌳", "Teorema de Pitágoras📐", "Conversión de Temperaturas🌡️"])
    
    if funciones == "Fórmula General🌳":
        st.header("Fórmula General🌳")
        a = st.number_input("Variable a", min_value=0.0, value=1.0)
        b = st.number_input("Variable b", min_value=0.0, value=1.0)
        c = st.number_input("Variable c", min_value=0.0, value=1.0)
        x1 = ((-b)+(((b**2)-(4*a*c))**(1/2)))/(2*a)
        x2 = ((-b)-(((b**2)-(4*a*c))**(1/2)))/(2*a)
        st.metric("X1= ", f"{x1:.2f}")
        st.metric("X2= ", f"{x2:.2f}")
        st.image("https://dicciomat.com/wp-content/uploads/2024/09/la-formula-general.png")
    
    elif funciones == "Teorema de Pitágoras📐":
        st.header("Teorema de Pitágoras📐")
        Cateto1 = st.number_input("Cateto 1: ", min_value=0, value=1)
        Cateto2 = st.number_input("Cateto 2: ", min_value=0, value=1)
        hipotenusa = math.sqrt(Cateto1**2 + Cateto2**2)
        st.metric("Hipotenusa: ", f"{hipotenusa:.2f}")
        st.image("https://www.smartick.es/blog/wp-content/uploads/2024/02/teorema-de-Pitagoras-2-1024x825.png")
     
    elif funciones == "Conversión de Temperaturas🌡️":
          st.header("Conversión de Temperaturas🌡️")
          celsius = st.slider("Grados Celsius: ", -100, 100, 0)
          conversion_a_farenheit = ((celsius * 9/5) + 32)
          st.metric("Conversión: ", f"{conversion_a_farenheit:.2f}")
          farenheit = st.slider("Grados Farenheit: ", -100, 100, 0)
          conversion_a_celsius = ((farenheit - 32) * 5/9)
          st.metric("Conversión: ", f"{conversion_a_celsius:.2f}")
          st.image("https://st4.depositphotos.com/15640006/20471/v/450/depositphotos_204711858-stock-illustration-vector-celsius-fahrenheit-meteorology-thermometers.jpg")
   


    



