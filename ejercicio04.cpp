#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <limits> 

using namespace std;

struct Temperatura {
    string fecha;
    double valor;
};

int main() {
    ifstream inputFile("registro_temperaturas.txt");
    ofstream outputFile("temperaturas_extremas.txt");

    string line;
    double temp_maxima = -numeric_limits<double>::infinity();
    double temp_minima = numeric_limits<double>::infinity();
    string fecha_maxima, fecha_minima;

    while (getline(inputFile, line)) {
        istringstream iss(line);
        string fecha_str;
        double valor;
        char delim;
        if (!(getline(iss, fecha_str, ',') && (iss >> valor >> delim))) {
            cerr << "Error: Formato de entrada incorrecto para la temperatura." << endl;
            continue;
        }

        if (valor > temp_maxima) {
            temp_maxima = valor;
            fecha_maxima = fecha_str;
        }
        if (valor < temp_minima) {
            temp_minima = valor;
            fecha_minima = fecha_str;
        }
    }

    outputFile << "Dia de temperatura maxima: " << fecha_maxima << ", " << temp_maxima << endl;
    outputFile << "Dia de temperatura minima: " << fecha_minima << ", " << temp_minima << endl;

    inputFile.close();
    outputFile.close();
    cout << "Los días con temperaturas extremas se han identificado y guardado en 'temperaturas_extremas.txt'." << endl;

    return 0;
}