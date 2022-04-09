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