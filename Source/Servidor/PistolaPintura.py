class pistola(object):
    def __init__(self, grosor=1, disparo=2, p='Pistola OFF'):
        self.set_grosor(grosor)
        self.set_disparo(disparo)
        self.pintando = p

    def set_disparo(self, disparo):
        
        if disparo == 1:
            self.tipodisparo = "Disparo circular"
            
        elif disparo == 2:
            self.tipodisparo = "Disparo lineal"
            
        elif disparo == 3:
            self.tipodisparo = "Disparo de precision"

        return self.get_tipo_disparo()
    
    def get_tipo_disparo(self):
        
        return self.tipodisparo

    def set_grosor(self, grosor):
        self.grosor = grosor
        return self.get_grosor()

    def get_grosor(self):
        return "Pintando con un grosor numero " + str(self.grosor)
    def encender(self):
        self.pintando = 'Pistola ON'
        return self.pintando

    def apagar(self):
        self.pintando = 'Pistola OFF'
        return self.pintando
    
    def __str__(self) :
        estado = str()
        estado += 'Estado Pistola: ' +self.pintando + '\n'
        estado += 'Tipo de Disparo: ' +self.get_tipo_disparo() + '\n'
        estado += 'Grosor de Disparo: ' +self.get_grosor() + '\n\n'
        return estado

        