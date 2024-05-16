#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <climits>
#include <limits>  
#include <iomanip> 

using namespace std;

struct Venta {
    string fecha;
    int monto;
};

int main() {
    ifstream inputFile("ventas_diarias.txt");
    ofstream outputFile("resumen_ventas.txt");

    Venta venta;
    int venta_total = 0;
    int venta_maxima = INT_MIN;
    int venta_minima = INT_MAX;
    string fecha_maxima, fecha_minima;

    while (getline(inputFile, venta.fecha, ',')) {
        inputFile >> venta.monto;
        inputFile.ignore(numeric_limits<streamsize>::max(), '\n');

        venta_total += venta.monto;

        if (venta.monto > venta_maxima) {
            venta_maxima = venta.monto;
            fecha_maxima = venta.fecha;
        }

        if (venta.monto < venta_minima) {
            venta_minima = venta.monto;
            fecha_minima = venta.fecha;
        }
    }

    double promedio_ventas = static_cast<double>(venta_total) / 5;

    outputFile << "Venta total: " << venta_total << endl;
    outputFile << "Promedio de ventas: " << fixed << setprecision(2) << promedio_ventas << endl;
    outputFile << "Dia de mayor venta: " << fecha_maxima << ", " << venta_maxima << endl;
    outputFile << "Dia de menor venta: " << fecha_minima << ", " << venta_minima << endl;

    inputFile.close();
    outputFile.close();
    cout << "El resumen de ventas se ha guardado en 'resumen_ventas.txt'." << endl;

    return 0;
}

