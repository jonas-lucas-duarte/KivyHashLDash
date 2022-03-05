# 03 EventosVariaveisInstancia

## Button

The Button is a Label with associated actions that are triggered when the button is pressed (or releasef after a click/touch). To configure the button, the same properties (padding, font_size, etc) and sizing system are used as for the Label class:

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

Ihf you want to be notified every time the button state changes, you can bind to the Button.state property:

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
