from datetime import datetime

class orden(object):
    def __init__(self,x = "Inicio de reporte"):
        now = datetime.now()
        self.now = now.strftime("%H:%M:%S")
        self.command = x
    
    def reportar(self):
        return str(self.command) + " a las " + str(self.now)
    
    def set_orden(self, x):
        now = datetime.now()
        self.command = x
        self.now = now.strftime("%H:%M:%S")

