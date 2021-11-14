
#como lo guardamos en la BD?
username_helper="""
MDTextField:
    hint_text:"Usuario"
    helper_text: "olvidaste el usuario?"
    helper_text_mode: "on_focus"
    pos_hint:{"center_x":0.5,"center_y":0.6}
    size_hint_x:None
    width:150
"""
#como lo guardamos en la BD?
password_helper="""
MDTextField:
    hint_text:"Contraseña"
    helper_text: "olvidaste la contraseña?"
    helper_text_mode: "on_focus"
    pos_hint:{"center_x":0.5,"center_y":0.5}
    size_hint_x:None
    width:150
"""

screen_helper = """
ScreenManager:
    pantallaMenu:
    pantallaConductor:
    pantallaPasajero:

<pantallaMenu>:
    name: "menu"
    MDRectangleFlatButton:
        text: "perfil"
        pos_hint:{"center_x":0.2,"center_y":0.2}
        on_press:root.manager.current="conductor"
    MDRectangleFlatButton:
        text: "Ser Conductor"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_press:root.manager.current="pasajero"
    MDRectangleFlatButton:
        text: "Ser Pasajero"
        pos_hint:{"center_x":0.5,"center_y":0.5}
        on_press:root.manager.current="pasajero"

<pantallaConductor>:
    name: "conductor"
    MDLabel:
        text: "hola jj"
        halign:"center"
    MDRectangleFlatButton:
        text: "volver"
        pos_hint:{"center_x":0.5,"center_y":0.3}
        on_press:root.manager.current="menu"
    MDRectangleFlatButton:
        text: "montar archivos"
        pos_hint:{"center_x":0.2,"center_y":0.3}
        on_press:root.manager.current="pasajero"

<pantallaPasajero>:
    name: "pasajero"
    MDLabel:
        text: "montar archivos"
        halign:"center"
    MDRectangleFlatButton:
        text: "volver"
        pos_hint:{"center_x":0.5,"center_y":0.2}
        on_press:root.manager.current="menu"
"""
