#ifndef CLI_CLIENTE_H
#define CLI_CLIENTE_H

#include <iostream>
using namespace std;

#include "Interfaz_RPC_Cliente.hh"



class Cli_Cliente
{
private:
    Interfaz_RPC_Cliente CLIENTE = Interfaz_RPC_Cliente();

public:
    Cli_Cliente(/* args */);
    ~Cli_Cliente();
    void Desplegar_Menu(); 
    string Pedir_Comadno();
    void Loop_Principal();
    bool Ejecutar_Respuesta(int comando);
    bool Interpretar_Comando(string comando);
    void Ayuda_Usuario();
};



#endif