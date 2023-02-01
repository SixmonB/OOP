from PanelControl_Servidor import PanelControl_Servidor as pc

class servidor(object):
    def __init__(self) :
        self.panel_control = pc()

    def iniciar(self):        
        self.panel_control.prompt = '>> '
        
        while(True):        
            self.panel_control.cmdloop('-------------',)

simon = servidor()
simon.iniciar()

