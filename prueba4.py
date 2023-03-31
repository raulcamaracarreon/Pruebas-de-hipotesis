import streamlit as st
from scipy.stats import t
def prueba_T_de_Student_para_dos_medias():
    st.title("Comparación de medias")
    st.write("Ingresa las medias y las bases de muestra para dos grupos, y se calculará el valor-p utilizando la prueba t de Student.")

    while True:
        # Obtener las medias y bases de muestra del usuario
        mean1 = st.number_input("Ingresa la media del primer grupo:", value=1.0, step=0.01, key="mean1")
        n1 = st.number_input("Ingresa la base de muestra del primer grupo:", value=10, step=1, key="n1")
        mean2 = st.number_input("Ingresa la media del segundo grupo:", value=1.0, step=0.01, key="mean2")
        n2 = st.number_input("Ingresa la base de muestra del segundo grupo:", value=10, step=1, key="n2")

        # Calcular el valor-p utilizando la prueba t de Student
        # Se asume varianzas iguales y una distribución normal de las muestras
        variance1 = st.number_input("Ingrese la varianza del primer grupo:", value=1.0, step=0.01, key="var1")
        variance2 = st.number_input("Ingrese la varianza del segundo grupo:", value=1.0, step=0.01, key="var2")

        stdev1 = variance1**0.5
        stdev2 = variance2**0.5

        pooled_std = ((n1-1) * stdev1**2 + (n2-1) * stdev2**2) / (n1 + n2 - 2)
        t_stat = (mean1 - mean2) / (pooled_std * (1/n1 + 1/n2)**0.5)
        p_value = 2 * (1 - t.cdf(abs(t_stat), n1 + n2 - 2))

        # Mostrar resultados
        st.write(f"Valor-p: {p_value:.4f}")
        if p_value < 0.05:
            st.write("La diferencia es estadísticamente significativa (p < 0.05)")
        else:
            st.write("La diferencia no es estadísticamente significativa (p > 0.05)")

        # Terminar el bucle
        break



