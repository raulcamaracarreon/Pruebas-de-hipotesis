import streamlit as st
import random
from scipy.stats import mannwhitneyu

def prueba_U_de_Mann_Whitney():
    st.title("Comparación de proporciones con el test de Mann-Whitney")
    st.write("Ingresa los porcentajes y bases de muestra para dos grupos, y se calculará el valor-p utilizando la función de Mann-Whitney U.")

    key = random.randint(0, 100000)

    while True:
        # Obtener porcentajes y bases de muestra del usuario
        p1 = st.number_input("Ingresa el primer porcentaje (ej. 0.60): ", min_value=0.0, max_value=1.0, step=0.0001, key='p1')
        n1 = st.number_input("Ingresa la base de muestra del primer porcentaje (ej. 100): ", min_value=1, step=1, key='n1')
        p2 = st.number_input("Ingresa el segundo porcentaje (ej. 0.70): ", min_value=0.0, max_value=1.0, step=0.0001, key='p2')
        n2 = st.number_input("Ingresa la base de muestra del segundo porcentaje (ej. 100): ", min_value=1, step=1, key='n2')


        # Generar las listas con las proporciones de éxito
        data1 = []
        data2 = []
        for i in range(int(n1)):
            if random.random() < p1:
                data1.append(1)
            else:
                data1.append(0)
        for i in range(int(n2)):
            if random.random() < p2:
                data2.append(1)
            else:
                data2.append(0)

        # Calcular el valor-p utilizando la función de Mann-Whitney U
        stat, p_value = mannwhitneyu(data1, data2)

        # Mostrar resultados
        st.write(f"Valor-p: {p_value:.4f}")
        if p_value < 0.05:
            st.write("La diferencia es estadísticamente significativa (p < 0.05)")
        else:
            st.write("La diferencia no es estadísticamente significativa (p > 0.05)")

        break

