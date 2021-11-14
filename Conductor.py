from Usuario import Usuario

#el metodo ocupado deberia ser atributo

class Pasajero:
    #constructor
    def __init__(self):
        self.parada="parada"
        self.licencia="xxxxxx"
        self.horario="00:00"

    #setter de la parada
    def setParada(self):
        #la api es la que le pregunta a donde ir
        #retorna string
        pass

    #setter del horario
    def setHorario(self,horario):
        self.horario=horario

    #getter del horario
    def getHorario(self):
        return self.horario

    #numero de cupos
    def numeroCupos(self):
        # este metodo deberia llamar a la capacidad del vehiculo e ir calculando
        #retona entero
        pass
#redundante lo de numero de cupos() y capacidad, no?
