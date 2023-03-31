import streamlit as st
import numpy as np
from scipy.stats import linregress

def prueba_regresion_lineal():
    st.title("Prueba de regresión lineal")

    # Obtener los datos de la muestra del usuario
    data = st.text_input("Ingresa los datos de la muestra -los datos de cada grupo separados por comas y los grupos separados por 'punto y coma'- (ej. 1, 2, 3; 4, 5, 6): ", value="1, 2, 3; 4, 5, 6")

    # Convertir los datos a una lista de listas de números
    data = [[float(x) for x in row.split(",")] for row in data.split(";")]

    # Calcular la regresión lineal utilizando la función linregress
    slope, intercept, r_value, p_value, std_err = linregress(data[0], data[1])

    # Mostrar resultados
    st.write(f"Pendiente de la recta de regresión: {slope:.4f}")
    st.write(f"Intercepto de la recta de regresión: {intercept:.4f}")
    st.write(f"Coeficiente de correlación: {r_value:.4f}")
    st.write(f"Valor-p: {p_value:.4f}")
    if p_value < 0.05:
        st.write("La regresión es significativa (p < 0.05)")
    else:
        st.write("La regresión no es significativa (p > 0.05)")
