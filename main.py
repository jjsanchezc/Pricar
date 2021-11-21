from kivy.properties import *
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import Screen
from Vehiculo import Vehiculo
from kivy.core.window import Window
from Usuario import Usuario
import mysql.connector
mysqlcnx = mysql.connector.connect(user='root', password='Daviddegea22.',
                              host='127.0.0.1',
                              database='pricar',
                              autocommit=True)
mysqlcursor=mysqlcnx.cursor()
mysqlcursor.execute("select * from empleados;")
mysqlresultado = mysqlcursor.fetchall()

# import request
api_file = open("Interfaz/API/aappii.txt", "r")
api_key = api_file.read()

#Window.size = (260, 500)
Window.size=(400,850)
v = Vehiculo()

#clase invocada
us=Usuario()



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
    def updateData(self):
        #mysqlcursor.execute("select * from empleados where empleados.CodigoTrabajador=" + us.getCode()+ ";")
        na = self.manager.get_screen("perfil")
        na.ids.nameP.text = us.getName()
        na.ids.mail.text = us.getMail()
        na.ids.address.text = us.getAddress()
        na.ids.cellphone.text = us.getCellphone()
        na.ids.placa.text = us.getPlaca()
        na.ids.carcap.text = str(us.getCarcap())
        na.ids.point.text = str(us.getPoints())

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
        cuentaExistente=False
        mysqlcursor.execute("select * from empleados;")
        mysqlresultado = mysqlcursor.fetchall()
        for user in mysqlresultado:
            if self.user.text == user[2]:
                self.codigo=user[0]
                mysqlcursor.execute("select * from empleados where empleados.CodigoTrabajador="+self.codigo+";")
                mysqlresultado = mysqlcursor.fetchall()
                for password in mysqlresultado:
                    if self.password.text==password[0]:
                        us.setCode(password[0])
                        us.setName(password[1])
                        us.setMail(password[2])
                        us.setCellphone(password[3])
                        us.setAddres(password[5])
                        us.setPlaca(password[6])
                        us.setCarcap(password[7])
                        us.setPoints(password[9])
                        cuentaExistente=True
                        na=self.manager.get_screen("perfil")
                        na.ids.nameP.text=us.getName()
                        na.ids.mail.text=us.getMail()
                        na.ids.address.text=us.getAddress()
                        na.ids.cellphone.text=us.getCellphone()
                        na.ids.placa.text=us.getPlaca()
                        na.ids.carcap.text=str(us.getCarcap())
                        na.ids.point.text=str(us.getPoints())


        #falta ver como se conecta con la base de datos y que revise todo eso
        if cuentaExistente==False:
            print("Datos incorrectos")
            self.show_popup("Datos incorrectos")
            #falta poner el popup que diga que "llene los campos
        elif cuentaExistente==True:
            kiv.current = "menu"
            print("hola ",self.user.text)


    def show_popup(self, title):
        show = ErrorLogin()
        self.popupWindow = Popup(title=title,title_size=25, content=show,
                                 size_hint=(None, None), size=(350, 300))
        self.popupWindow.open()


"""Clase de la pantalla de perfil"""


class ProfileScreen(Screen):
    pass



"""Clase de la pantalla de editar perfil"""
class EditProfileScreen(Screen):
    nameP=ObjectProperty(None)
    email=ObjectProperty(None)
    cel=ObjectProperty(None)
    placa=ObjectProperty(None)
    direc=ObjectProperty(None)
    capve=ObjectProperty(None)
    def save(self):
        #que reciba los datos que ingresó el usuario, si no ingresó nada no se cambia nada
        if self.nameP.text!="":
            us.editName(self.nameP.text)
        if self.email.text!="":
            us.editMail(self.email.text)
        if self.direc.text!="":
            us.editAddress(self.direc.text)
        if self.cel.text!="":
            us.editCellphone(self.cel.text)
        if self.placa.text!="":
            us.editPlaca(self.placa.text)
        if self.capve.text!="":
            us.editCarcap(self.capve.text)

        print("se ha guardado correctamente")

"""Pantalla predeterminada"""
class Default(Screen):
    pass

"""Clase de pantalla de pasajero"""
class RiderProfileScreen(Screen):
    pass

class DriverWNRScreen(Screen):
    pass
class DriverVPScreen(Screen):
    pass
class DriverPPScreen(Screen):
    pass
class RiderWNRScreen(Screen):
    pass
class RiderPScreen(Screen):
    pass
class RiderEndRScreen(Screen):
    pass
class RiderWaitScreen(Screen):
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
        self.popupWindow = Popup(title=title,title_size=25, content=show,
                                 size_hint=(None, None), size=(350,250))
        self.popupWindow.open()

if __name__ == "__main__":
    Pricar().run()


mysqlcnx.close()

