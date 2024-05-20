with open("notas.txt", "r") as inputFile:
   
    with open("promedios.txt", "w") as outputFile:
        
        for line in inputFile:
            
            parts = line.strip().split(",")
            nombre = parts[0]
            notas = [float(x.split(":")[1]) for x in parts[1:]]
            num_notas = len(notas)
            suma_notas = sum(notas)
            promedio = suma_notas / num_notas if num_notas > 0 else 0
            
            outputFile.write(f"{nombre}, Promedio: {promedio}\n")

print("Ok, completado. Ver 'promedios.txt'.")