import streamlit as st
import numpy as np
from scipy.stats import chi2_contingency

def prueba_chi_cuadrado():
    st.title("Prueba Chi-cuadrado")

    # Obtener los datos de la tabla de contingencia del usuario
    data = st.text_input("Ingresa los datos de la tabla de contingencia, -los datos de cada grupo separados por comas y los grupos separados por 'punto y coma'- (ej. 5, 10, 15; 20, 25, 30): ", value="5, 10, 15; 20, 25, 30")

    # Convertir los datos a una lista de listas de números
    data = [[int(x) for x in row.split(",")] for row in data.split(";")]

    # Realizar la prueba chi-cuadrado
    chi2, p_value, dof, expected = chi2_contingency(data)

    # Mostrar resultados
    st.write(f"Estadística de prueba chi-cuadrado: {chi2:.4f}")
    st.write(f"Valor-p: {p_value:.4f}")
    if p_value < 0.05:
        st.write("Hay una asociación significativa entre las variables (p < 0.05)")
    else:
        st.write("No hay una asociación significativa entre las variables (p > 0.05)")
