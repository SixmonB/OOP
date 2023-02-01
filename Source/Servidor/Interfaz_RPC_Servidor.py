    # from PanelControl_Servidor import PanelControl_Servidor
from xmlrpc.server import SimpleXMLRPCServer
from threading import Thread
import socket


#from PanelControl_Servidor import PanelControl_Servidor

class Interfaz_XML_RPC():
    server = None
    RPC_PORT = 8891
    
    def __init__(self, servidor, puerto=RPC_PORT):
        
        self.SERVIDOR = servidor
        self.puerto_usado = puerto
        
        while True:
            try:
                #Creacion del servidor indicando el puerto deseado
                self.server = SimpleXMLRPCServer(("localhost", self.puerto_usado), allow_none=True)
                
                if self.puerto_usado != puerto:
                    print(f'Servidor RPC ubicado en puerto no estandar [{puerto}]')
            
                break
            
            except socket.error as e:
                
                if e.errno == 98:
                    
                    self.puerto_usado += 1
                    continue

                else:
                    print('El servidor RPC no puede ser iniciado.')
                    raise

        # ------  REGISTRO DE FUNCIONES ------
        # AUTOMATICO - MOVER  - MANUAL - EFECTOR - ORIGEN - DEZPLAZAR - SET_ESTADO - GET_ESTADO - TIPO_DISPARO  - GROSOR_DISPARO - REPORTE
        self.server.register_function(self.Automatico, 'SECUENCIA')
        self.server.register_function(self.Mover, 'MOVER')
        self.server.register_function(self.Efector, 'EFECTOR')
        self.server.register_function(self.Origen, 'ORIGEN')
        self.server.register_function(self.Dezplazar, 'DEZPLAZAR')    
        self.server.register_function(self.Reporte, 'REPORTE')
        self.server.register_function(self.Add_Report, "ADD_REPORT")
        self.server.register_function(self.Conectar_Robot, "ACTIVAR")
        
        
        
        #Se lanza el Servidor
        self.thread = Thread(target=self.Run_Server)
        self.thread.start()

        print(f'El Servidor RPC se ha iniciado en el PUERTO [{str(self.server.server_address)}]')
                    
        

    
    def Run_Server(self):
        
        self.server.serve_forever()
        
    
    def Apagar(self):
        
        self.server.shutdown()
        self.thread.join()
    
    def __del__(self):
        self.server.shutdown()
        self.thread.join()
    
    def Mover(self, args):
               
        return str(self.SERVIDOR.do_mover(args))

    
    def Automatico(self,args):
        
        return self.SERVIDOR.do_automatico(args)
                
        
    def Efector(self,args):
        
        return self.SERVIDOR.do_efector(args) 

    def Origen(self,args):  
        
        return self.SERVIDOR.do_origen(args)
 

    def Dezplazar(self,args):
        
        return self.SERVIDOR.do_desplazar(args)

    
    def Conectar_Robot(self, args):
        return self.SERVIDOR.do_activar(args)


    
    def Reporte(self,args):
        return self.SERVIDOR.do_reportar('0 1')
    

    def Add_Report(self,args):
        return self.SERVIDOR.add_report(args)
    

    