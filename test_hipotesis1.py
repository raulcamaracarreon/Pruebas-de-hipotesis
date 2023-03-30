import streamlit as st
from prueba3 import prueba_U_de_Mann_Whitney
from prueba4 import prueba_T_de_Student_para_dos_medias
from prueba5 import prueba_T_de_Student_para_una_muestra
from prueba6 import test_de_Wilcoxon_de_medianas_para_una_muestra
from prueba7 import prueba_ANOVA
from prueba8 import prueba_chi_cuadrado
from prueba9 import prueba_correlacion
from prueba10 import prueba_regresion_lineal

st.set_page_config(page_title="Pruebas de hipótesis", page_icon=":chart_with_upwards_trend:")

# Pestañas
tabs = ["U de Mann Whitney", "Prueba T para dos medias", "Prueba T para una muestra", "Test de Wilcoxon", "ANOVA", "Chi-cuadrado", "Correlación", "Regresión lineal"]
active_tab = st.sidebar.radio("Seleccione una prueba de hipótesis:", tabs)

# Mostrar contenido según la pestaña seleccionada
if active_tab == "U de Mann Whitney":
    prueba_U_de_Mann_Whitney()
elif active_tab == "Prueba T para dos medias":
    prueba_T_de_Student_para_dos_medias()
elif active_tab == "Prueba T para una muestra":
    prueba_T_de_Student_para_una_muestra()
elif active_tab == "Test de Wilcoxon":
    test_de_Wilcoxon_de_medianas_para_una_muestra()
elif active_tab == "ANOVA":
    prueba_ANOVA()
elif active_tab == "Chi-cuadrado":
    prueba_chi_cuadrado()
elif active_tab == "Correlación":
    prueba_correlacion()
else:
    prueba_regresion_lineal()

