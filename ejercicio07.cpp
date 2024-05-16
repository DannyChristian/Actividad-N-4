#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <map>

using namespace std;

int main() {
    ifstream inputFile("archivo_log.txt");
    ofstream outputFile("resumen_errores.txt");

    map<string, int> conteo_errores;

    string line;
    while (getline(inputFile, line)) {
        if (line.find("ERROR") == 0) {
            // Encuentra el código de error en la línea
            size_t pos = line.find(":");
            if (pos != string::npos) {
                string error_code = line.substr(0, pos + 4); // Incluye ":"
                conteo_errores[error_code]++;
            }
        }
    }

    for (const auto& entry : conteo_errores) {
        outputFile << entry.first << ": " << entry.second << endl;
    }

    inputFile.close();
    outputFile.close();
    cout << "El resumen de errores se ha guardado en 'resumen_errores.txt'." << endl;

    return 0;
}
