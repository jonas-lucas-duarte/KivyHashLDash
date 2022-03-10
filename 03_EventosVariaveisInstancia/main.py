from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Test(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        
        # Aumentando o tamanho da fonte com font_size
        # Eventos de botão (on_release, on_press)
        button = Button(text='Botão 1', font_size=30, on_release=self.incrementar)

        # Aumentando o tamanho da fonte com font_size
        # Variável da Instância
        self.label = Label(text='1', font_size=30)

        box.add_widget(button)
        box.add_widget(self.label)
        
        return box

    # Método da classe
    def incrementar(self, button):
        #button.text = 'Soltei'
        # Incrementar o valor atual por um
        self.label.text = str(int(self.label.text) + 1)

Test().run()
