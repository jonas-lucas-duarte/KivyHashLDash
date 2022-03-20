# 04 LinguagemKivy

## Kivy Language

The Kivy language is a language dedicated to describing user interface and interactions. You could compare this language to Qt's QML (http://qt.nokia.com), but we included new concepts such as rule definitions (which are somewhat akin to what you may know from CSS), templationg and so on.

### Overview

The language consists of several constructs that you can use:

#### Rules:

A rule is similar to a CSS rule. A rule applies to specific widgets (or classes thereof) in your widget tree and modifies them in a certain way. You can use rules to specify interactive behaviour or use them to add graphical representations of the widgets they apply to. You can target a specific class of widgets (similar to the CSS concept of a class) by using the `cls` attribute (e.g. `cls=MyTestWidget`).

#### A Root Widget

You can use the language to create yout entire user interface. A kv file must contain only one root widget at most.

#### Dynamic Classes

Dynamic classes let you create new widgets and rules on-the-fly, without any Python declaration.

#### Templates

Templates were used to populate parts of an application, such as styling the content of a list. They are now deprecated by dynamic classes.

### Syntax of a kv File

A Kivy language file must have `.kv` as filename extension.

The content of the file should always start with the Kivy header, where *version* must be replaced with the Kivy language version you're using. For now, use 1.0:

```python
#:kivy `1.0`

# content here
```

The *content* can contain rule definitions, a root widget, dynamic class definitions and templates:

```python
# Syntax of a rule definition. Note that several Rules can share the same
# definition (as in CSS). Note the braces: they are part of the definition.
<Rule1, Rule2>:
	# .. definitions ..

<Rule3>:
	# .. definitions ..

# Syntax for creating a root widget
RootClassName:
	# .. definitions ..

# Syntax for creating a dynamic class
<NewWidget@BaseClass>:
	# .. definitions ..

# Syntax for create a template
[TemplateName@BaseClass1, BaseClass2]:
	# .. definitions ..
```

Regardless of whether it's a rule, root widget, dynamic class or template you're defining, the definition should look like this:

```python
# With the braces it's a rule. Without them, it's a root widget.
<ClassName>:
	prop1: value1
	prop2: value2

	canvas:
		CanvasInstruction1:
			canvasprop1: value1
		CanvasInstruction2:
			canvasprop2: value2

	AnotherClass:
		prop3: value1
```

Here *prop1* and *prop2* are the properties of *ClassName* and *prop3* is the property of *AnotherClass*. If the widget doesn't have a property with the given name, an `ObjectProperty` will be automatically created and added to the widget.

*AnotherClass* will be created and added as a child of the *ClassName* instance.

- The indentation is important and must be consistent. The spacing must be a multiple of the number of spaces used on the first indented line. Spaces are encouraged: mixing tabs and spaces is not recommended.

- The value of a property must be given on a single line (for now at least).

- Keep class names capitalized to avoid syntax errors.

- The *canvas* property is special: you can put graphics instructions in it to create a graphical representation of the current class.

Here is a simple example of a kv file that contains a root widget:

```python
#:kivy 1.0

Button:
	text: 'Hello world'
```

Both the `load_file()` and the `load_string()` methods return the root widget defined in your kv file/string. They will also add any class and template definitions to the `Factory` for later usage.

### Value Expressions, on_property Expressions, ids, and Reserved Keywords

When you specify a property's value, is evaluated as a Python expression. This expression can be static or dynamic, which means that the value can use the values of other properties using reserved keywords.

##### self

The keyword self references the "current widget instance":

```python
Button:
	text: 'My state is %s' % self.state
```

##### root

This keyword is available only in rule definitions and represents the root widget of the rule (the first instance of the rule):

```python
<MyWidget>:
	custom: 'Hello world'
	Button:
		text: root.custom
```

##### app

This keyword always refers to your app instance. It's equivalent to a call to `kivy.app.App.get_running_app()` in Python.

```python
Label:
	text: app.name
```

##### args

This keyword is available in on_<action> callbacks. It refers to the arguments passed to the callback.

```python
TextInput:
	on_focus: self.insert_text("Focus" if args[1] else "No focus")
```

https://kivy.org/doc/stable/api-kivy.lang.html
