#include "Cli_cliente.hh"

Cli_Cliente::Cli_Cliente(/* args */)
{
}
 
Cli_Cliente::~Cli_Cliente()
{
}

void Cli_Cliente::Desplegar_Menu(){
    
    
    cout << endl
         << "Seleccione una Orden:" << endl
         << endl
         << "==========================" << endl
         << "- ACTIVAR ROBOT ---------| A:0/1 (off/on)" << endl
         << "- MOVER   ---------------| M:x,y,z" << endl
         << "- DESPLAZAR -------------| D:x,y" << endl
         << "- SECUENCIA AUTOMATICA --| S:" << endl
         << "- EFECTOR ---------------| E:0/1 (off/on)" << endl
         << "- ORIGEN ----------------| O: " << endl        
         << "- REPORTE----------------| R: " << endl         
         << "- AYUDA  ----------------| H: " << endl
         << "- SALIR  ----------------| Quit" << endl
         << "==========================" << endl
         << endl;
}



string Cli_Cliente::Pedir_Comadno(){
    
    string buffer;
    this->Desplegar_Menu();
    cin >> buffer;
    return buffer;
}

bool Cli_Cliente::Interpretar_Comando(string comando){
    
    bool Orden_valida = false;
    string orden;
    
    switch (comando[0])
    {
        
        //MOVER
        case 'M':
        case 'm':
            Orden_valida = true;
            orden = "MOVER";            
            break;
        
        //MOVER
        case 'd':
        case 'D':
            Orden_valida = true;
            orden = "DEZPLAZAR";            
            break;
        //ACTIVAR
        case 'A':
        case 'a':
            Orden_valida = true;
            orden = "ACTIVAR";            
            break;

        //EFECTOR
        case 'E':
        case 'e':            
            Orden_valida = true;
            orden =  "EFECTOR";            
            break;
        
        //REPORTE
        case 'R':
        case 'r':
            Orden_valida = true;
            orden = "REPORTE";            
                        
            break;
        
        //ORIGEN
        case 'o':
        case 'O':
            Orden_valida = true;
            orden = "ORIGEN";                                    
            break;
        
        //SALIR
        case 'Q':
        case 'q':
            cout << "Seleccionaste SALIR, adios" << endl;
            return false;
            
        //AYUDA
        case 'H':
        case 'h':
            
            Orden_valida = false;
            this->Ayuda_Usuario();
            break;

        //AUTOMATICO
        case 'S':
        case 's':
            Orden_valida = true;
            orden = "SECUENCIA";                                    
            break;
    
    default:
        cout << "El comando ingresado es INVALIDO" << endl;
        break;
    }

    if (Orden_valida)
    {
        string parametro;        
        if (comando.length() > 2){
         
            parametro = comando.substr(2);
        }
        else
        {            
            parametro = "Sin Argumento";
        }
        
        this->CLIENTE.Ejecutar_Orden(orden, parametro);
    }
    
    return true;

}

void Cli_Cliente::Loop_Principal(){
    
    string orden;
    bool continuar = true;
    while(continuar){
        
        orden = this->Pedir_Comadno();
        continuar = this->Interpretar_Comando(orden);
        cout << "Presione <ENTER> para continuar...." << endl;
        _getch();
    }
    
    return;
}

void Cli_Cliente::Ayuda_Usuario(){

    cout << endl
         << "AYUDA DE FUNCIONES PARA CLIENTE:" << endl
         << endl
         << "==============================================" << endl
         << "1- ACTIVAR ROBOT ---------| A:0/1 (off/on)" << endl
         << "Activa o Desactiva el ROBOT segun corresponda [1/0]" << endl
         << endl
         << "2- MOVER  ----------------| M:x,y,z" << endl
         << "Mueve EFECTOR final segun coordenadas x,y,z atraves de articulaciones" << endl
         << endl
         << "3- DESPLAZAR -------------| D:x,y" << endl
         << "Desplazamiento (x,y) de la base del robot" << endl
         << endl
         << "4- SECUENCIA AUTOMATICA --| A:" << endl
         << "Carga archivo .txt con secuencia de ordenes preestablecidas " << endl
         << endl
         << "5- EFECTOR ---------------| E:0/1 (off/on)" << endl
         << "Abre o Cierra [1/0] valvula de pintura" << endl
         << endl
         << "6- ORIGEN ----------------| O: " << endl
         << "Vuelve a la posicion de default" << endl
         << endl
         << "7- REPORTE ---------------| R: " << endl
         << "Entrega un reporte compuesto por ESTADO ACTUAL del robot e historial de ordenes desde inicio" << endl
         << "==============================================" << endl;         


}



int main(int argc, char const *argv[])
{
    Cli_Cliente cli = Cli_Cliente();
    cli.Loop_Principal();
    return 0;
}
