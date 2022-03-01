from kivy.app import App
from kivy.uix.button import Button

# Importando BoxLayout (Objeto Layout: empilha os widgets como caixas)
from kivy.uix.boxlayout import BoxLayout

# Importando Label (Objeto Tabela)
from kivy.uix.label import Label

class Test(App):
    def build(self):
        # Instanciando Classe
        box = BoxLayout(orientation='vertical')
        button = Button(text='Botão 1')
        label = Label(text='Texto 1')
        
        # Adicionando widgets em Layout
        box.add_widget(button)
        box.add_widget(label)

        # Instanciando Classe2
        box2 = BoxLayout()

        button2 = Button(text='Botão 2')
        label2 = Label(text='Texto 2')

        # Adicionando widgets em Layout2
        box2.add_widget(button2)
        box2.add_widget(label2)

        # Adicionando Layout dentro do Layout
        box.add_widget(box2)

        return box

Test().run()
