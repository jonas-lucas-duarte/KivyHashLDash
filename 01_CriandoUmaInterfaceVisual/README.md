# 01 CriandoUmaInterfaceVisual

[![HashLDash](https://i.ytimg.com/vi/WiyF3VsL5dY/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLBrJHPAIsNA7_lXzKemzsKhB-LlNw)](https://youtu.be/WiyF3VsL5dY "01 Criando Uma Interface Visual")

## App

The App class is the base for creating Kivy applications. Think of it as your main entry point into the Kivy run loop. In most cases, you subclass this class and make your own app. You create an instance of your specific app class and then, when you are ready to start the application's life cycle, you call your instance's App.run() method.

### run()

Lauches the app in standalone mode.

https://kivy.org/doc/stable/api-kivy.app.html

## Button

The Button is a Label with associated actions that are triggered when the button is pressed (or released after a click/touch). To configure the button, the same properties (padding, font_size, etc) and sizing system are used as for the Label class:

```python
button = Button(text='Hello world', font_size=14)
```

To attach a callback when the button is pressed (clicked/touched), use bind:

```python
def callback(instance):
	print('The button <%s> is being pressed' % instance.text)

btn1 = Button(text='Hello world 1')
btn1.bind(on_press=callback)
btn2 = Button(text='Hello world 2')
btn2.bind(on_press=callback)
```

If you want to be notified every time the button state changes, you can bin to the Button.state property:

```python
def callback(instance, value):
	print('My button <%s> state is <%s>' % (instance, value))

btn1 = Button(text='Hello world 1')
btn1.bind(state=callback)
```

Kv Example:

```python
Button:
	text: 'press me'
	on_press: print("ouch! More gently please")
	on_release: print("ahhh")
	on_state: print("my current state is {}".format(self.state))
```

### text (FROM LABEL)

Text of the label.

Creation of a simple hello world:

```python
widget = Label(text='Hello world')
```

If you want to create the widget with an unicode string, use:

```python
widget = Label(text=u'My unicode string')
```

text is a StringProperty and defaults to `´.

https://kivy.org/doc/stable/api-kivy.uix.button.html
