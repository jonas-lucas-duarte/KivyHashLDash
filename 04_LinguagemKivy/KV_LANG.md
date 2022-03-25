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

https://kivy.org/doc/stable/guide/lang.html
