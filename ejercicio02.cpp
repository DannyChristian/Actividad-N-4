#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

int main() {
    ifstream inputFile("notas.txt");
    ofstream outputFile("promedios.txt");

    string line;
    while (getline(inputFile, line)) {
        istringstream iss(line);
        string nombre, materia;
        double nota, sumaNotas = 0;
        int numNotas = 0;
        char delim1 = ',', delim2 = ':';

        getline(iss, nombre, delim1);
        
        while (getline(iss, materia, delim2)) {
            iss >> nota;
            sumaNotas += nota;
            numNotas++;
            if (iss.peek() == delim1) {
                iss.ignore();
            }
        }

        double promedio = (numNotas > 0) ? sumaNotas / numNotas : 0;
        outputFile << nombre << delim1 << " Promedio: " << promedio << endl;
    }

    inputFile.close();
    outputFile.close();

    cout << "Ok, completado vea 'promedios_estudiantes.txt'." << endl;

    return 0;
}