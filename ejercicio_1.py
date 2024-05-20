
with open("datos_personales.txt", "r") as inputFile:
   
    with open("emails_filtrados.txt", "w") as outputFile:
       
        for line in inputFile:
           
            nombre, edad, email = line.strip().split(",")
           
            edad = int(edad)
            
            if edad > 18:
           
                outputFile.write(email + "\n")

print("Ok, revisa 'emails_filtrados.txt'.")
