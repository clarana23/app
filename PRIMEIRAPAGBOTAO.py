from kivy.app import App

from kivy.uix.button import Button

from kivy.uix.relativelayout import RelativeLayout

from kivy.config import Config

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager

from kivy.uix.label import Label


class Gerenciador(ScreenManager):
    pass

Config.set('graphics', 'resizable', True)


class Pos_Size_App(App):

    def build(self):

        rl = RelativeLayout(size=(300, 300))
        box = BoxLayout(orientation='vertical')
        label = Label(text='Texto 1')
        box.add_widget(label)
        b1 = Button(size_hint=(.2, .2),
                    pos_hint={'center_x': .5, 'center_y': .8},
                    text="Cliente",
                    background_color = (0,0, 1, 1))
        b2 = Button(size_hint=(.2, .2),
                    pos_hint={'center_x': .5, 'center_y': .5},
                    text="Transportador ADM",
                    background_color = (0,0, 1, 1))

        b3 = Button(size_hint=(.2, .2),
                    pos_hint={'center_x': .5, 'center_y': .2},
                    text="Motorista",
                    background_color=(0, 0, 1, 1))

        rl.add_widget(b1)
        rl.add_widget(b2)
        rl.add_widget(b3)

        return rl


if __name__ == "__main__":
    Pos_Size_App().run() 