# 03 EventosVariaveisInstancia

[![HashLDash](https://i.ytimg.com/vi/XwvtHW_XN-A/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLBQdUhTznkzg6fkzruLOvRAz-iZ0w)](https://youtu.be/XwvtHW_XN-A "03 Eventos Variáveis Intância")

## Label

The `Label` widget is for rendering text:

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

`font_size` is a `NumericProperty` and defaults to 15sp.

https://kivy.org/doc/stable/api-kivy.uix.label.html

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