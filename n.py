import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Título de la aplicación
st.title('Prueba de Hipótesis para Diferencia de Medias (Muestras Independientes)')

# Entrada de datos de las muestras
st.header('Ingreso de Datos')
sample1 = st.text_input('Muestra 1 (separada por comas)', '12,11,14,13,13,14,13,12,14,12')
sample2 = st.text_input('Muestra 2 (separada por comas)', '13,10,11,12,13,12,10,12')

# Conversión de entradas a listas de números
sample1 = np.array(list(map(float, sample1.split(','))))
sample2 = np.array(list(map(float, sample2.split(','))))

# Cálculo de estadísticas básicas
mean1, mean2 = np.mean(sample1), np.mean(sample2)
std1, std2 = np.std(sample1, ddof=1), np.std(sample2, ddof=1)
n1, n2 = len(sample1), len(sample2)

# Nivel de significancia
alpha = st.slider('Nivel de Significancia (α)', 0.01, 0.10, 0.05, 0.01)

# Selección de tipo de hipótesis alternativa
st.header('Tipo de Hipótesis Alternativa')
hypothesis_type = st.radio('Seleccione el tipo de hipótesis alternativa:',
                           ['Unilateral Derecha', 'Unilateral Izquierda', 'Bilateral'])

# Cálculo de Z-score y valor crítico
pooled_std = np.sqrt((std1**2 / n1) + (std2**2 / n2))
z_score = (mean1 - mean2) / pooled_std

# Determinación del valor crítico y la región de aceptación/rechazo
if hypothesis_type == 'Unilateral Derecha':
    critical_value = stats.norm.ppf(1 - alpha)
    decision = 'Rechazar H0' if z_score > critical_value else 'No Rechazar H0'
    region = 'Derecha'
elif hypothesis_type == 'Unilateral Izquierda':
    critical_value = stats.norm.ppf(alpha)
    decision = 'Rechazar H0' if z_score < critical_value else 'No Rechazar H0'
    region = 'Izquierda'
else:  # Bilateral
    critical_value = stats.norm.ppf(1 - alpha/2)
    decision = 'Rechazar H0' if abs(z_score) > critical_value else 'No Rechazar H0'
    region = 'Ambos lados'

# Mostrar resultados
st.subheader('Resultados')
st.write(f'Z-score calculado: {z_score:.4f}')
st.write(f'Valor crítico: {critical_value:.4f}')
st.write(f'Decisión: {decision}')
st.write(f'Región de rechazo: {region}')

# Gráfico de la distribución de probabilidad
x = np.linspace(-4, 4, 1000)
y = stats.norm.pdf(x, 0, 1)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Distribución Normal', color='blue')
plt.axvline(z_score, color='green', linestyle='--', label='Z-score')

# Configuración de las líneas de la región de rechazo
if hypothesis_type == 'Unilateral Derecha':
    plt.axvline(critical_value, color='red', linestyle='--', label='Valor crítico')
    plt.fill_between(x, y, where=(x > critical_value), color='red', alpha=0.3, label='Región de rechazo (derecha)')
elif hypothesis_type == 'Unilateral Izquierda':
    plt.axvline(critical_value, color='red', linestyle='--', label='Valor crítico')
    plt.fill_between(x, y, where=(x < critical_value), color='red', alpha=0.3, label='Región de rechazo (izquierda)')
else:  # Bilateral
    plt.axvline(critical_value, color='red', linestyle='--', label='Valor crítico positivo')
    plt.axvline(-critical_value, color='red', linestyle='--', label='Valor crítico negativo')
    plt.fill_between(x, y, where=(x > critical_value), color='red', alpha=0.3, label='Región de rechazo (derecha)')
    plt.fill_between(x, y, where=(x < -critical_value), color='red', alpha=0.3, label='Región de rechazo (izquierda)')

plt.title('Distribución de la Prueba de Hipótesis')
plt.xlabel('Z')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
st.pyplot(plt)
