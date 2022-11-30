from kivy.app import App

from kivy.uix.label import Label

from kivy.properties import NumericProperty

from kivy.core.audio import SoundLoader

from kivy.animation import Animation



class refeicaorelogio(Label):
    a = NumericProperty(4200)  # seconds

    def start(self):
        Animation.cancel_all(self)  # stop any current animations
        self.anim = Animation(a=0, duration=self.a)

        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "Tempo de refeição finalizado"
            sound = SoundLoader.load('pern.mp3')
            if sound:
                sound.play()

        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def on_a(self, instance, value):
        self.text = str(round(value, 1))


class ref(App):
    def build(self):
        crudeclock = refeicaorelogio()
        crudeclock.start()
        return crudeclock

if __name__ == '__main__':
    ref().run()