import streamlit as st
import math
from collections import Counter

def calcular_entropia(texto):
    
    contador = Counter(texto)
    
    longitud_total = len(texto)
    
    probabilidades = [frecuencia / longitud_total for frecuencia in contador.values()]
    
    entropia = -sum(p * math.log2(p) for p in probabilidades)
    
    return entropia

st.title('Cálculo de Entropía de un Archivo de Texto')

archivo_subido = st.file_uploader('Sube un archivo de texto', type='txt')

if archivo_subido is not None:
    
    contenido = archivo_subido.read().decode('utf-8')
    st.text_area('Contenido del archivo', contenido, height=300)
    entropia = calcular_entropia(contenido)
    st.write(f'La entropía del contenido del archivo es: {entropia}')
