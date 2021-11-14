from kivy.properties import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import Screen

from Vehiculo import Vehiculo
from kivy.core.window import Window
# import request
api_file = open("Interfaz/API/aappii.txt", "r")
api_key = api_file.read()

Window.size = (260, 500)
v = Vehiculo()
#WIDGETS, POPUPS
"""popup para avisar que hubo un error en el login"""
class ErrorLogin(FloatLayout):
    pass
"""popup para editar perfil"""
class EditPerfil(FloatLayout):
    def moveTo(self):
        kiv.current = "editP"

    #aun no funciona este metodo
    def close(self):
        EditPerfil.exit()

#SCREEN, SCREEN MANAGER, MAIN
"""Clase de la pantalla del menu"""
class MenuScreen(Screen):
    pass

"""Clase de la pantalla del conductor"""
class DriverScreen(Screen):
    pass

"""Clase de la pantalla del pasajero"""
class RiderScreen(Screen):
    pass

"""Clase de la pantalla de login"""
class LogInScreen(Screen):
    user=ObjectProperty(None)
    password=ObjectProperty(None)
    def login(self):
        #falta ver como se conecta con la base de datos y que revise todo eso
        if self.user.text is "" or "@h.com" not in self.user.text or self.password.text is "":
            print("Datos incorrectos")
            self.show_popup("Datos incorrectos")
            #falta poner el popup que diga que "llene los campos
        elif self.user.text != "" and "@h.com" in self.user.text and self.password.text is not "":
            kiv.current = "menu"
            print("hola ",self.user.text)

    def show_popup(self, title):
        show = ErrorLogin()
        self.popupWindow = Popup(title=title, content=show,
                                 size_hint=(None, None), size=(250, 200))
        self.popupWindow.open()



    """    
    Clase de la pantalla de perfil
      
    falta poner lo de si quieres configurar tu cuenta por favor presiona en "si"
    de lo contrario poner no. tonces qu si se presiona si, que lo mande a la pagina de CreateProfileScreen
    juntar con base de datos """

"""Clase de la pantalla de perfil"""
class ProfileScreen(Screen):
    #cada valor lo debe traer la base de datos de la persona
    nombre=ObjectProperty("")
    correo=StringProperty()
    direccion=StringProperty()
    celular=StringProperty()

"""Clase de la pantalla de editar perfil"""
class EditProfileScreen(Screen):
    """Este metodo guardará los cambios que se le hicieron al perfil
        falta conectarlo a la base de datos"""
    def save(self):
        print("se ha guardado correctamente")

"""Pantalla predeterminada"""
class Default(Screen):
    pass

"""Clase de pantalla de pasajero"""
class RiderProfileScreen(Screen):
    pass


#WINDOWMANAGER
class WindowManager(ScreenManager):
    pass
kiv = Builder.load_file(("Interfaz/main.kv"))

"""MAIN"""
class Pricar(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return kiv

    def show_popup(self,title):
        show = EditPerfil()
        self.popupWindow = Popup(title=title, content=show,
                                 size_hint=(None, None), size=(250, 250))
        self.popupWindow.open()
    """que aca tenga una opcion de modificar datos, para que se pueda actualizar todo
    juntar con base de datos"""
if __name__ == "__main__":
    Pricar().run()

