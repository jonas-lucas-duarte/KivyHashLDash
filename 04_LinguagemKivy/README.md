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
