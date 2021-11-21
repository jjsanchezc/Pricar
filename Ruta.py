import webbrowser
from Pasajero import *
#importar las cosas de la api

pasa=Pasajero()
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


    #setter del punto final de la ruta del conductor
    def setPuntoFinal(self,punto):
        self.puntoFinal=punto


    #getter punto inicial
    def getPuntoInicial(self):
        return self.puntoInicial

    #getter punto final
    def getPuntoFinal(self):
        #retorna string, le damos la ubicacion del "trabajo"
        return self.puntoFinal

    #metodo para crear la ruta que va a tener el conductor hacia el trabajo
    def crearRuta(self):
        url=("https://www.waze.com/ul?ll=",self.getPuntoFinal(),)
        webbrowser.open("https://www.waze.com/ul?ll=6.20020215%2C-75.5784848084993&navigate=no&zoom=17&from=6.2657%2C-75.5682")

    #agrega una parada a la ruta del conductor para que pueda recoger a las personas
    def agregarParada(self):
        """cuando el conductor acepta el viaje, se le debe de agregar una
        parada a la ruta."""
        pass
