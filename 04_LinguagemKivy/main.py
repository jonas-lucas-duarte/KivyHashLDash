from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# Criando um Widget (que herda de BoxLayout = Widget)
class Incrementador(BoxLayout):
    # Funcionalidade em linguagem Kivy
    pass

class Test(App):
    def build(self):
        # Instância do Widget
        return Incrementador()

Test().run()
