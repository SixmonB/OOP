#include "Interfaz_RPC_Cliente.hh"

Interfaz_RPC_Cliente::Interfaz_RPC_Cliente(/* args */){
   
}

Interfaz_RPC_Cliente::~Interfaz_RPC_Cliente()
{

}


bool Interfaz_RPC_Cliente::Ejecutar_Orden(string orden, std::string parametro){
    
    
    bool continuar = true;
    string buffer_temp = orden + " " + parametro;

    const char *comando = orden.c_str();
    const char *argumento = parametro.c_str();
    this->oneArg[0] = buffer_temp.c_str();
    this->CLIENTE.execute("ADD_REPORT", this->oneArg[0], this->result);

    this->oneArg[0] = argumento;

    if (this->CLIENTE.execute(comando, this->oneArg[0], this->result))
            std::cout << this->result << "\n\n";
    else
        std::cout << "Error en la llamada a "<<comando<<"\n\n";
    continuar = true;
        

    return continuar;
}





