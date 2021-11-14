#importar las cosas de la api
from main import Pricar

class Ruta():
    #constructor
    def __init__(self):
        self.puntoInicial=""
        self.puntoFinal=""
        """yo creo que en vez de hacer un setter y 
        getter, podemos asignarle el valor de una"""

    #setter del punto inicial del conductor
    def setPuntoInicial(self,punto):
        #define el punto inicial
        self.puntoInicial=punto
        pass

    #setter del punto final de la ruta del conductor
    def setPuntoFinal(self,punto):
        self.puntoFinal=punto
        pass

    #getter punto inicial
    def getPuntoInicial(self):
        return self.puntoInicial

    #getter punto final
    def getPuntoFinal(self):
        #retorna string, le damos la ubicacion del "trabajo"
        return self.puntoFinal

    #metodo para crear la ruta que va a tener el conductor hacia el trabajo
    def crearRuta(self):
        #ver como funciona la api y asi poder retornar la ruta
        pass

    #agrega una parada a la ruta del conductor para que pueda recoger a las personas
    def agregarPara(self):
        """cuando el conductor acepta el viaje, se le debe de agregar una
        parada a la ruta."""
        pass