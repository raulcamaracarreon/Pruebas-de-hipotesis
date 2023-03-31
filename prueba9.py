import streamlit as st
import numpy as np
from scipy.stats import pearsonr, spearmanr

def prueba_correlacion():
    st.title("Prueba de correlación")

    # Obtener los datos de la muestra del usuario
    data = st.text_input("Ingresa los datos de la muestra -los datos de cada grupo separados por comas y los grupos separados por 'punto y coma'- (ej. 1, 2, 3; 4, 5, 6): ", value="1, 2,3 ; 4, 5, 6")

    # Convertir los datos a una lista de listas de números
    data = [[float(x) for x in row.split(",")] for row in data.split(";")]

    # Obtener el tipo de correlación deseado
    correlation_type = st.selectbox("Seleccione el tipo de correlación:", ["Pearson", "Spearman"])

    # Calcular la correlación utilizando el tipo seleccionado
    if correlation_type == "Pearson":
        correlation, p_value = pearsonr(data[0], data[1])
    else:
        correlation, p_value = spearmanr(data[0], data[1])

    # Mostrar resultados
    st.write(f"Coeficiente de correlación: {correlation:.4f}")
    st.write(f"Valor-p: {p_value:.4f}")
    if p_value < 0.05:
        st.write("La correlación es significativa (p < 0.05)")
    else:
        st.write("La correlación no es significativa (p > 0.05)")
