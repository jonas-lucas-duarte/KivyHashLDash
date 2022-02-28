# Importando App (Objeto Principal)
from kivy.app import App

# Importando Button (Objeto Botão)
from kivy.uix.button import Button

# Herança de App
class Test(App):
    # Método para inicializar e construir o App
    def build(self):
        return Button(text='Olá Mundo!!')

# Instância da Classe Herdada de App
Test().run()

