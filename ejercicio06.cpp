#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

int main() {
    ifstream inputFile;
    inputFile.open("registro_horas.txt");

    ofstream outputFile;
    outputFile.open("informe_horas.txt");
    
    map<string, int> horas_trabajadas;

    string line;
    while (getline(inputFile, line)) {
        istringstream iss(line);
        string nombre;
        int horas;
        char delim;
        if (!(getline(iss, nombre, ',') && (iss >> horas >> delim))) {
            cerr << "Error: Formato de entrada incorrecto para las horas trabajadas." << endl;
            continue;
        }
        horas_trabajadas[nombre] += horas;
    }

    for (const auto& entry : horas_trabajadas) {
        outputFile << entry.first << ", Horas Totales: " << entry.second << endl;
    }

    inputFile.close();
    outputFile.close();
    cout << "El informe de horas totales se ha guardado en 'informe_horas.txt'." << endl;

    return 0;
}