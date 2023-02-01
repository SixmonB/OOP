#ifndef INTERFAZ_RPC_CLIENTE_H
#define INTERFAZ_RPC_CLIENTE_H

#include <iostream>
#include <string>
using namespace std;

#include <conio.h>
#include "XmlRpc.h"
using namespace XmlRpc;






class Interfaz_RPC_Cliente
{
private:
    
    XmlRpcClient CLIENTE = XmlRpcClient("127.0.0.1", 8891);
    XmlRpcValue noArgs, result, oneArg;

public:
    
    Interfaz_RPC_Cliente();
    ~Interfaz_RPC_Cliente();

    bool Enviar_Peticion(std::string orden);
    bool Ejecutar_Orden(string comadno, std::string parametro);
};


#endif