import streamlit as st
from scipy.stats import f_oneway

def prueba_ANOVA():
    st.title("Prueba de ANOVA")

    # Obtener los datos de la muestra del usuario
    data = st.text_input("Ingresa los datos de la muestra, separados por comas (ej. 1,2,3;4,5,6;7,8,9): ", value="1,2,3;4,5,6;7,8,9")

    # Convertir los datos a una lista de listas de números
    data = [[float(x) for x in row.split(",")] for row in data.split(";")]

    # Realizar la prueba ANOVA
    stat, p_value = f_oneway(*data)

    # Mostrar resultados
    st.write(f"Valor F: {stat:.4f}")
    st.write(f"Valor-p: {p_value:.4f}")
    if p_value < 0.05:
        st.write("Hay diferencias significativas entre las medias de los grupos (p < 0.05)")
    else:
        st.write("No hay diferencias significativas entre las medias de los grupos (p > 0.05)")
