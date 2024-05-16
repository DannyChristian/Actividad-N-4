#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>

using namespace std;

int main() {
    ifstream inputFile("precios_dolares.txt");
    ofstream outputFile("precios_soles.txt"); 
    const double tasa_conversion = 3.85;
    string line;
    while (getline(inputFile, line)) {
        istringstream iss(line);
        string producto;
        double precio_dolares;
        if (!(getline(iss, producto, ',') && (iss >> precio_dolares))) {
            cerr << "Error: Formato de entrada incorrecto para el precio del producto." << endl;
            continue;
		}      
        double precio_soles = precio_dolares * tasa_conversion;
        outputFile << producto << ", " << fixed << setprecision(2) << precio_soles << endl;
    }
    inputFile.close();
    outputFile.close();
    cout << "Los precios se han convertido y guardado en 'precios_soles.txt'." << endl;

    return 0;
}