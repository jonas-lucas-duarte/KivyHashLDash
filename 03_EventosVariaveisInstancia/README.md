# 03 EventosVariaveisInstancia

## Label

The Label widget is for rendering text. It supports ascii and unicode string:

```python
# hello world text
l = Label(text='Hello world')

# unicode text; can only display glyphs that are availabel in the font
l = Label(text=u'Hello world' + unichr(2764))

# multiline text
l = Label(text='Multi\nLine')

# size
l = Label(text='Hello world', font_size='20sp')
```

### font_size

Font size of the text, in pixels.

font_size is a NumericProperty and defaults to 15sp.

https://kivy.org/doc/stable/api-kivy.uix.label.html

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

If you want to be notified every time the button state changes, you can bind to the Button.state property:

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

### font_size (FROM LABEL)

Font size of the text, in pixels.

font_size is a NumericProperty and defaults to 15sp.

https://kivy.org/doc/stable/api-kivy.uix.button.html

---

## Metrics

**A screen is defined by its physical size, density and resolution. These factors are essential for creating UI's with correct size everywhere.**

**In Kivy, all the graphics pipelines work with pixels. But using pixels as a measurement unit is problematic because sizes change according to the screen.**

### Dimensions

**If you want to design you UI for different screen sizes, you will want better measurement units to work with. Kivy provides some more scable alternatives**

#### Units

*sp*

**Scale-independent Pixels - This is like the dp unit, but it is also scaled by the user's font size preference. We recommend you use this unit when specifying font sizes, so the font size will be adjusted to both the screen density and the user's preference.**

https://kivy.org/doc/stable/api-kivy.metrics.html

---

## Button Behavior

**The ButtonBehavior mixin class provides Button behavior. You can combine this class with other widgets, such as an Image, to provide alternative buttons that preserve Kivy button behavior.**

**For an overview of behaviors, please refer to the behaviors documentation.**

### Events

*on_press*

**Fired when the button is pressed**

*on_release*

**Fired when the button is released (i.e. the touch/click that pressed the button goes away).**
