class articulacion(object):
    def __init__(self, name, angulo=90, x=0, y=0):
        self.name = name
        self.angulo = angulo
        self.posx = x
        self.posy = y
        self.origen = 90

    def default(self):
        self.angulo = self.origen
        self.posx = 0
        self.posy = 0

    def set_angulo(self, angulo):
        self.angulo = angulo

    def get_angulo(self):
        return self.angulo

    def get_posicion(self):
        return "(" + str(self.posx) + ", " + str(self.posy) + ")"
    def desplazar(self, x, y):
        self.posx = x
        self.posy = y
        return "Base desplazada a la posicion (" + str(x) + ", " + str(y) + ")"
