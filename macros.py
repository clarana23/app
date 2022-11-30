from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.app import App

from kivy.uix.label import Label

from kivy.properties import NumericProperty

from kivy.core.audio import SoundLoader

from kivy.animation import Animation

from banheiro import banheiro

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        size_hint: .8,.8
        pos_hint: {'left': 0.5}
        
        Button:
            text: 'Abastecimento'
            on_press: root.manager.current = 'abastecimento'           
        Button:
            text: 'WC'
            on_press: root.manager.current = 'wc'
        Button:
            text: 'Refeição'
            on_press: root.manager.current = 'refeicao'
            
        Button:
            text: 'Manutenção'
            on_press: root.manager.current = 'manutencao'
            
        Button:
            text: 'Pernoite'
            on_press: root.manager.current = 'pernoite'
        
        Button:
            text: 'Pânico'            
            
            
<abastecimentoScreen>:
    BoxLayout:
        Button:
            text: 'Pânico'
        Button:
            text: 'Reiniciar rota!'
            on_press: root.manager.current = 'menu'
            
<wcScreen>:
    BoxLayout:
        Button:
            text: 'Pânico'
        Button:
            text: 'Reiniciar rota!'
            on_press: root.manager.current = 'menu'
            
<refeicaoScreen>:
    BoxLayout:
        Button:
            text: 'Pânico'
        Button:
            text: 'Reiniciar rota!'
            on_press: root.manager.current = 'menu'
            
<manutencaoScreen>:
    BoxLayout:
        Button:
            text: 'Pânico'
        Button:
            text: 'Reiniciar rota!'
            on_press: root.manager.current = 'menu'

<pernoiteScreen>:
    BoxLayout:
        Button:
            text: 'Pânico'
        Button:
            text: 'Reiniciar rota!'
            on_press: root.manager.current = 'menu'
""")


class MenuScreen(Screen):
    pass


class abastecimentoScreen(Screen):
    pass


class wcScreen(Screen):
    pass

class refeicaoScreen(Screen):
    pass


class manutencaoScreen(Screen):
    pass


class pernoiteScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(abastecimentoScreen(name='abastecimento'))
        sm.add_widget(wcScreen(name='wc'))
        sm.add_widget(refeicaoScreen(name='refeicao'))
        sm.add_widget(manutencaoScreen(name='manutencao'))
        sm.add_widget(pernoiteScreen(name='pernoite'))

        return sm


if __name__ == '__main__':
    TestApp().run()
