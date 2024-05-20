
with open("registro_horas.txt", "r") as inputFile:
   
    with open("informe_horas.txt", "w") as outputFile:
        
        horas_trabajadas = {}

        
        for line in inputFile:
            
            nombre, horas_str = line.strip().split(",")
            horas = int(horas_str)

            
            if nombre in horas_trabajadas:
                horas_trabajadas[nombre] += horas
            else:
                horas_trabajadas[nombre] = horas

        
        for nombre, horas in horas_trabajadas.items():
            outputFile.write(f"{nombre}, Horas Totales: {horas}\n")

print("El informe de horas totales se ha guardado en 'informe_horas.txt'.")
