import streamlit as st
import numpy as np
from scipy.stats import wilcoxon

def test_de_Wilcoxon_de_medianas_para_una_muestra():
    st.title("Test de Wilcoxon de medianas para una muestra")

    # Obtener los datos de la muestra del usuario
    data = st.text_input("Ingresa los datos de la muestra, separados por comas (ej. 1,2,3): ", value="1,2,3")

    # Convertir los datos a una lista de números
    data = [float(x) for x in data.split(",")]

    # Verificar si el tamaño de muestra es suficientemente grande
    if len(data) < 2:
        st.warning("Se recomienda un tamaño de muestra mínimo de 2 para realizar el test de medianas.")

    # Obtener el valor de la mediana poblacional hipotética del usuario
    pop_median = st.number_input("Ingresa la mediana poblacional hipotética: ", value=0.0, step=0.01)

    # Calcular el valor-p utilizando el test de medianas de Wilcoxon
    stat, p_value = wilcoxon(np.array(data) - pop_median)

    # Mostrar resultados
    st.write(f"Valor-p: {p_value:.4f}")
    if p_value < 0.05:
        st.write("La mediana de la muestra es significativamente diferente de la mediana poblacional hipotética (p < 0.05)")
    else:
        st.write("La mediana de la muestra no es significativamente diferente de la mediana poblacional hipotética (p > 0.05)")

