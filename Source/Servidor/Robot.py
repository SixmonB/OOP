from Articulacion import articulacion
from PistolaPintura import pistola

class Robot(object):

    Q_ARTICULACIONES = 3 
    def __init__(self):
        
        self.pistolita = pistola(1,1)
        self.art = []
        self.estado = False    


        for i in range(self.Q_ARTICULACIONES+1):
            self.art.append(articulacion(i))
            #art[1] es la base que se mueve en el piso
            #art[2:6] articulaciones propiamente

    def check(self):
        if self.estado == True:
            return True
        else:
            return False

    def mover(self, x, y, z):
        """(x,y,z) son las coordenadas deseadas del efector final. La cuenta realizada para cada articulacion es simbolica"""
        if self.check():
            angulos = list()
            for a in range(1,self.Q_ARTICULACIONES + 1):
                self.art[a].set_angulo(int((x+y+z)*pow((a*2/5),2)))
                angulos.append(self.art[a].get_angulo())
            
            return "Articulaciones rotadas: " + str(angulos)
        else:
            return "Robot DESACTIVADO"
    
    def desplazamiento(self,x,y):
        if self.check():
            return(self.art[0].desplazar(x,y))
        else:
            return "Robot DESACTIVADO"
    def pintar(self, a=0):
        """pintar(1) enciende y pintar(0) apaga"""
        if self.check():
            if a == 1:
                return(self.pistolita.encender())
            else:
                return(self.pistolita.apagar())
        else:
            return "Robot DESACTIVADO"


    def grosor(self, g):
        return(self.pistolita.set_grosor(g))

    def tipo(self, t):
        return(self.pistolita.set_disparo(t))

    def get_estado(self):
        if self.estado == True:
            x = "ACTIVADO"
        else:
            x = "DESACTIVADO"
        return("Estado del robot: " + x)
    
    def get_estado_pistola(self):
        return str(self.pistolita)


    def return_origen(self):
        """coordenadas de origen definidas por el fabricante"""
        if self.check():
            angulos = list()
            self.art[0].default()
            for a in range(1,self.Q_ARTICULACIONES+1):
                self.art[a].default()
                angulos.append(self.art[a].get_angulo())
            return "Articulaciones en posicion de origen " + str(angulos)
        else:
            return "Robot DESACTIVADO"

    def set_estado(self, bool):
        self.estado = bool
        if self.estado == True:
            x = "ACTIVADO"
        else:
            x = "DESACTIVADO"
        return("Estado del robot: " + x)

    def get_estado_articulaciones(self):
        estado =str()
        for b in range(1,self.Q_ARTICULACIONES+1):
            estado += f"Posicion de la articulacion ({b}) = " + str(self.art[b].get_angulo()) + "\n"
        estado += f"Posicion de la de la BASE = " + str(self.art[0].get_posicion()) + "\n"
        return estado

    def __str__(self):

        estado = str()
        estado += self.get_estado() + '\n\n'
        estado += self.get_estado_pistola()
        estado += self.get_estado_articulaciones() + '\n'
        return estado


