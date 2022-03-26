# KV LANG

Programming Guide

## Concept behind the language

As yout application grows more complex, it's common that the construction of widget trees and explicit declaration of binding becomes verbose and hard to maintain. The *KV* Language is an attempt to overcome these shortcomings.

The *KV* language, sometimes called kvlang or the kivy language, allows you to create your widget tree in a declarative way and to bind widget properties to each other or to callbacks in a natural manner. It allows for very fast prototypes and agile changes to your UI. It also facilitates separating the logic of yout application and its User Interface.

## How to load KV

There are two ways to load Kv code into yout application:

- By name convention:

Kivy looks for a Kv file with the same name as your App class in lowercase, minus "App" class if it ends witl 'App' e.g:

```python
MyApp -> my.kv
```

If this file defines a *Root Widget* it will be attached to the App's *root* attribute and used as the base of the applicayion widget tree.

- `Builder`: You can tell Kivy to directly load a string or a file. If this string or file defines a root widget, it will be returned by the method:

```python
Builder.load_file('path/to/file.kv')
```

or 

```python
Builder.load_string(kv_string)
```

## Rule context

A Kv source constitutes of *rules* which are used to describe the content of a Widget. You can hvae one *root* rule, and any number of *class* or *template* rules.

The *root* rule is declared by declaring the class of yout root widget, without any indentation, followed by *:* and will be set as the *root* attribute of the App instance:

```python
Widget:
```

A *class* rule, delcared by the name of a widget class between < > and followed by *:*, defines the appearance and behavior of any instance of that class:

```python
<MyWidget>:
```

Rules use indentation for delimitation, like Python. Indentation should be four spaces per level, like the Python style guide [recommends](https://github.com/jonas-lucas-duarte/KivyHashLDash/blob/main/04_LinguagemKivy/PEP_8.md)

There are three keywords specific to the Kv language:

- *app*: always refers to the instance of yout application.

- *root*: refers to the base widget/template in the current rule

- *self*: always refer to the current widget

## Instantiate children

To declare a widget instance of some class as a child widget, just declare that child inside the rule:

```python
MyRootWidget:
	BoxLayout:
		Button:
		Button:
```

The example above defines that our root widget, an instance of *MyRootWidget*, has a child that is an instance of the `BoxLayout`, and that BoxLayout further has two children, instances of hte `Button` class.

The Python equivalent of this code might be:

```python
root = MyRootWidget()
box = BoxLayout()
box.add_widget(Button())
box.add_widget(Button())
root.add_wiget(box)
```

Which you may find less nice, both to read and to write.

Of course, in Python, you can pass keyword arguments to yout widgets at creation to specify their behaviour. For example, to set the number of columns of a `gridlayout`, we would do:

```python
grid = GridLayout(cols=3)
```

To do the same thing in kv, you can set properties of the child widget directly in the rule:

```python
GridLayout:
	cols: 3
```

The value is evaluated as a Python expression, and all the properties used in the expression will be observed, that means that if you had something like this in Python (this assume *self* is a widget with a *data* `ListProperty`):

```python
grid = GridLayout(cols=len(self.data))
self.bind(data=grid.setter('cols'))
```

To have your display updated when your data change, you can now have just:

```python
GridLayout:
	cols: len(root.data)
```

Note

Widget names should start with upper case letters while property names should start with lower case ones. Following the [PEP8 Naming Conventions](https://github.com/jonas-lucas-duarte/KivyHashLDash/blob/main/04_LinguagemKivy/PEP_8.md) is encouraged.

## Event Bindings

You can bind to events in Kv using the ":" systanx, that is, associating a callback to an event:

```python
Widget:
	on_size: my_callback()
```

You can pass the values dispatched by the signal using the *args* keyword:

```python
TextInput:
	on_text: app.search(args[1])
```

More complex expressions can be used, like:

```python
pos: self.center_x - self.texture_size[0] / 2., self.center_y - self.textura_size[1] / 2.
```

This expression listens for a change in `center_x`, `center_y`, and `texture_size`. If one of them changes, the expression will be re-evaluated to update the `pos` field.

You can also handle `on_` events inside your kv language. For example the TextInput class has a `focus` property whose auto-generated `on_focus` event can be accessed inside the kv language like so:

```python
TextInput:
	on_focus: print(args)
```

## Referencing Widgets

In a widget tree there is ofthen a need to access/reference other widgets. The Kv Language provides a way to do this using id's. Think of them as class level variables that can only be used in the Kv language. Consider the following:

```python
<MyFirstWidget>:
	Button:
		id: f_but
	TextInput:
		text: f_but.state

<MySecondWidget>:
	Button:
		id: s_but
	TextInput:
		text: s_but.state
```

An `id` is limited in scope to the rule it is declared in, so in the code aboce `s_but` can not be accessed outside the `<MySecondWidget>` rule.

> Warning
>
> When assigning a value to `id`, remeber that the value isn't a string. There are no quotes: good -> `id: value`, bad -> `id: 'value'`

An `id` is a `weakref` to the widget and not the widget itself. As a consequence, storing the `id` is not sufficient to keep the widget from being garbage colleted. To demonstrate:

```python
<MyWidget>:
	label_widget: label_widget
	Button:
		text: 'Add Button'
		on_press: root.add_widget(label_widget)
	Button:
		text: 'Remove Button'
		on_press: root.remove_widget(label_widget)
	Label:
		id: label_widget
		text: 'widget'
```

Although a reference to `label_widget` is stored in `MyWidget`, it is not sufficient to keep the object alivev once other references have been removed because it's only a weakref. Therefore, after the remove button is clicked (which removes any direct reference to the widget) and the window is resized (which calls the garbage collector resulting in the deletion of `label_widget`), when the add button is clicked to add the widget back, a `ReferenceError: weakly-referenced object no longer exists` will be thrown. 

To keep the widget alive, a direct reference to the `label_widget` widget must be kept. This is achieved usind `id.__self__` or `label_widget.__self__` in this case. The correct way to do would be:

```python
<MyWidget>:
	label_widget: label_widget.__self__
```

https://kivy.org/doc/stable/guide/lang.html
