
class Temperatura:
    def __init__(self, fecha, valor):
        self.fecha = fecha
        self.valor = valor


with open("registro_temperaturas.txt", "r") as inputFile:
    
    with open("temperaturas_extremas.txt", "w") as outputFile:
        
        temp_maxima = float('-inf')
        temp_minima = float('inf')
        fecha_maxima = ""
        fecha_minima = ""

       
        for line in inputFile:
            
            fecha, valor_str = line.strip().split(",")
            valor = float(valor_str)

            
            if valor > temp_maxima:
                temp_maxima = valor
                fecha_maxima = fecha

            
            if valor < temp_minima:
                temp_minima = valor
                fecha_minima = fecha

        
        outputFile.write(f"Día de temperatura máxima: {fecha_maxima}, {temp_maxima}\n")
        outputFile.write(f"Día de temperatura mínima: {fecha_minima}, {temp_minima}\n")

print("Los días con temperaturas extremas se han identificado y guardado en 'temperaturas_extremas.txt'.")
