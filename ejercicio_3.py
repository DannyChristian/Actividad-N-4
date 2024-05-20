
with open("precios_dolares.txt", "r") as inputFile:
   
    with open("precios_soles.txt", "w") as outputFile:
        
        tasa_conversion = 3.85
      
        for line in inputFile:
            
            parts = line.strip().split(",")
            
            producto = parts[0]
            precio_dolares = float(parts[1])
            
            precio_soles = precio_dolares * tasa_conversion
            
            outputFile.write(f"{producto}, {precio_soles:.2f}\n")

print("Los precios se han convertido y guardado en 'precios_soles.txt'.")
