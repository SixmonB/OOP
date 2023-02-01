from cmd import Cmd
from Robot import Robot
from Orden import orden
from Interfaz_RPC_Servidor import Interfaz_XML_RPC as RPC
import time

class PanelControl_Servidor(Cmd):
    pintor = Robot()
    orden1 = orden()
    reporte = []
    hora = []
    last = 0
    indice = 0
    INTERFAZ_RPC = None
    
    def __Abrir_Archivo(self,ruta):

 
        archivo = open(ruta,'r')
        
        lista_ordenes = list()
        for linea in archivo:
            linea = linea.replace('\n','')        
            lista_ordenes.append(linea)
        
        archivo.close()
        return lista_ordenes
    def __Armar_Orden(self,orden):
    
        switcher = {
            'M':'do_mover(args)',
            'E':'do_efector(args)',
            'O':'do_origen(args)',
            'D': 'do_desplazar(args)',
            'D': 'do_desplazar(args)',            
        }

        comando = switcher[orden[0]]
        comando = comando.replace('args',f"'{orden[2:]}'")
        comando = 'self.'+comando
        return comando

    def mover(self, move):
        move = move
        x= self.pintor.mover(int(move[0]), int(move[1]), int(move[2]))
        print(x)
        return x

    def do_mover(self,args):
        """Mueve EFECTOR final segun coordenadas x,y,z atraves de articulaciones"""
        movimiento = args.split(',')
        
        return PanelControl_Servidor.mover(self,movimiento)

    def do_automatico(self,args):
        """Carga archivo .txt con secuencia de ordenes preestablecidas """

        lista_ordenes = self.__Abrir_Archivo('secuencia_automatica.txt')
            
        respuesta = str()
        for orden in lista_ordenes:
            comando_ejecutar = self.__Armar_Orden(orden)        
            respuesta += eval(comando_ejecutar)+'\n'
        self.do_reportar('0')
        return respuesta

    def do_efector(self,args):
        """Abre o Cierra [1/0] valvula de pintura"""
        x = self.pintor.pintar(int(args))
        print(x)
        return x

    def do_desplazar(self, args):
        """Desplazamiento (x,y) de la base del robot"""
        desp = args.split(',')
        x = self.pintor.desplazamiento(int(desp[0]), int(desp[1]))
        print(x)
        return x

    def do_origen(self,args):       
        """origen vuelve a la posicion de default"""
        x = self.pintor.return_origen()
        print(x)
        return x

    def do_manual(self,args):
        """manual mueve articulacion a posicion (x,y,z) y luego pinta"""
        manual = args.split()
        x = PanelControl_Servidor.mover(self, manual)+'\n'
        y = PanelControl_Servidor.do_efector(self, 1)
        return str(x+y)

    def do_activar(self,args):
        """Activa o Desactiva el ROBOT segun corresponda [1/0]"""
        if args == '0':
            x =self.pintor.set_estado(False)
            print(x)
            return x
        else:            
            x = self.pintor.set_estado(True)
            print(x)
            return x
    
    def do_get_estado(self,args):
        """consulta estado del robot"""
        x = str(self.pintor)
        print(x)
        return x

    def do_tipo_disparo(self, args):
        """set tipo de disparo
        1: disparo circular
        2: disparo lineal
        3: disparo de precision"""
        x = self.pintor.tipo(int(args))
        print(x)
        return x

    def do_conexion_remota(self, args):
        """Inicia El servidor RPC para conexion remota [0:DESCONECTAR - 1:CONEXION] """
        
        if args == '1':

            self.INTERFAZ_RPC = RPC(self)
     
        elif args == '0': 

            if self.INTERFAZ_RPC:           
                self.INTERFAZ_RPC.Apagar()
                del(self.INTERFAZ_RPC)
                self.INTERFAZ_RPC = False
                print("El servidor fue desconectado")

    def do_grosor_disparo(self,args):
        """set grosor de disparo de 1 (mas fino) a 9 (mas grueso)"""
        print(self.pintor.grosor(int(args)))

    def do_reportar(self,args):
        """Entrega un reporte compuesto por ESTADO ACTUAL del robot e historial de ordenes desde inicio"""
        
        REPORTE = '\nREPORTE\n-------------------\n\n'
        REPORTE += str(self.pintor)
        
        REPORTE += '-------\n'
        REPORTE += 'Historial de ORDENES\n'
        for a in range(self.last):                
                
            REPORTE += f'[{self.hora[a]}]  {self.reporte[a]} \n'
        print(REPORTE)
        return REPORTE
        
        
    def add_report(self,report):
        self.orden1.set_orden('[cliente]: '+report)
        self.reporte.append(self.orden1.command)
        self.hora.append(self.orden1.now)
        self.last += 1
        return self.reporte, self.hora


    def default(self,args):
        print("Error. El comando \'" + args + "\' no existe")
        self.reporte.pop()
        self.hora.pop()
        self.last -= 1
        return 'hola'

    def precmd(self,args):
        args = args.lower()
        self.orden1.set_orden(args)
        self.reporte.append("[servidor] " + self.orden1.command)
        self.hora.append(self.orden1.now)
        self.last += 1
        return (args)

    def do_quit(self,args):
        """quit sale del interprete"""
        print("Sistema Cerrado")
        
        raise SystemExit