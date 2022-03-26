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

https://kivy.org/doc/stable/guide/lang.html
