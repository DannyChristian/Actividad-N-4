#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

int main() {
    std::ifstream inputFile("datos_personales.txt");  // Archivo de entrada
    std::ofstream outputFile("emails_filtrados.txt"); // Archivo de salida

    std::string line;
    while (std::getline(inputFile, line)) {
        std::istringstream iss(line);
        std::string nombre, email;
        int edad;
        char delim; 
        std::getline(iss, nombre, ',');
        iss >> edad >> delim;
        std::getline(iss, email);
        if (edad > 18) {
            outputFile << email << std::endl;
        }
    }

    inputFile.close();
    outputFile.close();

    std::cout << "Ok revisar: 'emails_filtrados.txt'." << std::endl;

    return 0;
}