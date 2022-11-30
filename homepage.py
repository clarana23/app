from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App

from kivymd.app import MDApp


Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Cliente'
            on_press: root.manager.current = 'cliente'              
        Button:
            text: 'Transportador ADM'
            on_press: root.manager.current = 'transpadm'
        Button:
            text: 'Motorista'
            on_press: root.manager.current = 'motorista'


<clienteScreen>:
    BoxLayout:
        Button:
            text: 'Pânico'
        Button:
            text: 'Reiniciar rota!'
            on_press: root.manager.current = 'menu'

<transpadmScreen>:
    BoxLayout:
        Button:
            text: 'Pânico'
        Button:
            text: 'Reiniciar rota!'
            on_press: root.manager.current = 'menu'

<motoristaScreen>:
    BoxLayout:
        Button:
            text: 'Pânico'
        Button:
            text: 'Reiniciar rota!'
            on_press: root.manager.current = 'menu'

""")


# Declare both screens
class MenuScreen(Screen):
    pass


# -------------------------------------------------------------------------------------
# FUNÇÃO CADASTRO DE USUARIO CLIENTE

class clienteScreen(Screen):
    class App(MDApp):
        pass

# ------------------------------------------------------------------------------------------------
# FUNÇÃO CADASTRO DE USUARIO TRASNP ADM

class transpadmScreen(Screen):
    class App(MDApp):
        pass

# ------------------------------------------------------------------------------------------------
# FUNÇÃO CADASTRO DE USUARIO MOTORISTA

class motoristaScreen(Screen):
    class App(MDApp):
        pass

# ------------------------------------------------------------------------------------------------
# FUNÇÃO QUE CHAMA TODAS AS OUTRAS CLASSES

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(clienteScreen(name='cliente'))
        sm.add_widget(transpadmScreen(name='transpadm'))
        sm.add_widget(motoristaScreen(name='motorista'))

        return sm

if __name__ == '__main__':
    TestApp().run()
