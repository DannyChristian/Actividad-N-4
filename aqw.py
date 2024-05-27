import numpy as np

# Generar 300 números enteros aleatorios entre 1 y 500
datos = np.random.randint(1, 501, size=300)

# Guardar los datos en un archivo de texto
with open("datos_enteros.txt", "w") as file:
    for dato in datos:
        file.write(f"{dato}\n")

print("Se han generado y guardado los datos enteros en 'datos_enteros.txt'.")