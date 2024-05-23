import streamlit as st
import pandas as pd

# Función para leer el archivo de texto y convertirlo en una lista de números
def leer_archivo(file):
    numeros = []
    for line in file:
        for num in line.split():
            try:
                numeros.append(int(num))
            except ValueError:
                st.error(f"El valor '{num}' no es un número entero válido.")
    return numeros

# Función para crear una tabla de distribución de frecuencias
def tabla_frecuencias(numeros):
    frecuencia = pd.Series(numeros).value_counts().sort_index().reset_index()
    frecuencia.columns = ['Número', 'Frecuencia']
    return frecuencia

st.title("Tabla de Distribución de Frecuencias")

# Subida de archivo
uploaded_file = st.file_uploader("Sube un archivo de texto", type="txt")

if uploaded_file is not None:
    st.write("Contenido del archivo:")
    content = uploaded_file.read().decode("utf-8")
    st.text(content)

    # Procesar el archivo
    numeros = leer_archivo(content.splitlines())
    if numeros:
        # Crear y mostrar la tabla de distribución de frecuencias
        tabla = tabla_frecuencias(numeros)
        st.write("Tabla de Distribución de Frecuencias:")
        st.dataframe(tabla)
    else:
        st.error("El archivo no contiene números válidos.")
else:
    st.info("Por favor, sube un archivo de texto.")
