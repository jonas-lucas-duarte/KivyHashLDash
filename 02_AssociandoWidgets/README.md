# 02 AssociandoWidgets

## BoxLayout

BoxLayout arranges children in a vertical or horizontal box.

To position widgets above/below each other, use a vertical BoxLayout:

```python
layout = BoxLayout(orientation='vertical')
btn1 = Button(text='Hello')
btn2 = Button(text='World')
layout.add_widget(btn1)
layout.add_widget(btn2)
```

To position widgets next to each other, use a horizontal BoxLayout. In this example, we use 10 pixel spacing between children; the first button covers 70% of the horizontal space, the second covers 30%:

```python
layout = BoxLayout(spacing=10)
btn1 = Button(text='Hello', size_hint=(.7, 1))
btn2 = Button(text='World', size_hint=(.0, 1))
layout.add_widget(btn1)
layout.add_widget(btn2)
```

Position hints are partially working, depending on the orientation:

* If the orientation is vertical: x, right and center_x will be used.
* If the orientation is horizontal: y, top and center_y will be used.

Kv Example:

```python
BoxLayout:
	orientation: 'vertical'
	Label:
		text: 'this on top'
	Label:
		text: 'this right aligned'
		size_hint_x: None
		size: self.texture_size
		pos_hint: {'right': 1}
	Label:
		text: 'this on bottom'
```

### add_widget(widget, index=0, canvas=None) (FROM WIDGET)

Add a new widget as a child of this widget.

#### widget: Widget

Widget to add to out list of children.

#### index: int, defaults to 0

Index to insert the widget in the list. Notice that the default of 0 means the widget is inserted at the beginning of the list and will thus be drawn on top of other sibiling widgets. For a full discussion of the index and widget hierarchy, please see the Widget Programming Guide.

#### canvas: str, defaults to None

Canvas to add widget's canvas to. Can be `before´, `after´ or None for the default canvas.

```python
from kivy.uix.button import Button
from kivy.uix.slider import Slider
root = Widget()
root.add_widget(Button())
slider = Slider()
root.add_widget(slider)
```

https://kivy.org/doc/stable/api-kivy.uix.boxlayout.html

## Label
