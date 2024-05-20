
class Venta:
    def __init__(self, fecha, monto):
        self.fecha = fecha
        self.monto = monto


with open("ventas_diarias.txt", "r") as inputFile:
  
    with open("resumen_ventas.txt", "w") as outputFile:
      
        ventas = []
        venta_total = 0
        venta_maxima = float('-inf')
        venta_minima = float('inf')
        fecha_maxima = ""
        fecha_minima = ""

     
        for line in inputFile:
           
            fecha, monto_str = line.strip().split(",")
            monto = int(monto_str)

            
            venta = Venta(fecha, monto)
            ventas.append(venta)

            
            venta_total += monto

            
            if monto > venta_maxima:
                venta_maxima = monto
                fecha_maxima = fecha

            
            if monto < venta_minima:
                venta_minima = monto
                fecha_minima = fecha

        
        promedio_ventas = venta_total / len(ventas)

        
        outputFile.write(f"Venta total: {venta_total}\n")
        outputFile.write(f"Promedio de ventas: {promedio_ventas:.2f}\n")
        outputFile.write(f"Día de mayor venta: {fecha_maxima}, {venta_maxima}\n")
        outputFile.write(f"Día de menor venta: {fecha_minima}, {venta_minima}\n")

print("El resumen de ventas se ha guardado en 'resumen_ventas.txt'.")