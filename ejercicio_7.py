
with open("archivo_log.txt", "r") as inputFile:
    
    with open("resumen_errores.txt", "w") as outputFile:
        
        conteo_errores = {}

        
        for line in inputFile:
            if line.startswith("ERROR"):
                
                pos = line.find(":")
                if pos != -1:
                    error_code = line[:pos + 1]  # Incluye ":"
                    conteo_errores[error_code] = conteo_errores.get(error_code, 0) + 1

       
        for error_code, count in conteo_errores.items():
            outputFile.write(f"{error_code}: {count}\n")

print("El resumen de errores se ha guardado en 'resumen_errores.txt'.")
