import streamlit as st
import numpy as np
from scipy.stats import ttest_1samp
def prueba_T_de_Student_para_una_muestra():
    st.title("Prueba t de Student para una muestra")

    # Obtener los datos de la muestra del usuario
    data = st.text_input("Ingresa los datos de la muestra, separados por comas (ej. 1,2,3): ")

    # Convertir los datos a una lista de números
    data = [float(x) for x in data.split(",")]

    # Verificar si el tamaño de muestra es suficientemente grande
    if len(data) < 2:
        st.warning("Se recomienda un tamaño de muestra mínimo de 2 para realizar la prueba t.")

    # Obtener el valor de la media poblacional hipotética del usuario
    pop_mean = st.number_input("Ingresa la media poblacional hipotética: ", value=0.0, step=0.01)

    # Calcular el valor-p utilizando la prueba t de Student
    stat, p_value = ttest_1samp(data, pop_mean)

    # Mostrar resultados
    st.write(f"Valor-p: {p_value:.4f}")
    if p_value < 0.05:
        st.write("La media de la muestra es significativamente diferente de la media poblacional hipotética (p < 0.05)")
    else:
        st.write("La media de la muestra no es significativamente diferente de la media poblacional hipotética (p > 0.05)")
