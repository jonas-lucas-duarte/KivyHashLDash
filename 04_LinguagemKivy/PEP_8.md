# PEP 8

This document gives conventions for the Python code comprising the standard libary in the main Python distribution.

## Code Lay-out

### Indentation

Use 4 spaces per indentation level.

Continuation lines should align wrapped elements either vertically using Python's implicit line joining inside parentheses, brackets and braces, or using a *hanging indent*. When using a hanging indent the following should be sonsidered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line:

```python
# Correct:

# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
  			 var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
def long_function_name(
		var_one, var_two, var_three,
		var_four):
	print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
	var_one, var_two,
	var_theree, var_four)
```

```python
# Wrong:

# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, ver_two,
	var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
	var_one, var_two, var_three,
	var_four):
	print(var_one)
```

The 4-space rule is optional for continuations lines.

Optional:

```python
# Hanging indents *may* be indented to other than 4 spaces.
foo = long_function_name(
  var_one, var_two,
  var_three, var_four)
```

When the conditional part of a an `if`-statement is long enough to require that it be written across multiple lines, it's worth nothing that the combination of a two character keyword (i.e. `if`), plus a single space, plus an opening parenthesis creates a natural 4-spaces indent for the subsequent lines of the multiline conditional. This can produce a visual conflict with the indented suite of code nested inside the `if`-statement, which would also naturally be indented to 4 spaces. This PEP takes no explicit position on how (or whether) to further visually distinguish such conditional lines from the nested suite inside the `if`-statement. Acceptable options in this situation include, but are not limited to:

```python
# No extra indentation.
if (this_is_one_thing and
	that_is_another_thing):
	do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
	that_is_another_thing):
	# Since both conditions are true, we can frobnicate.
	do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
		and that_is_another_thing):
	do_something()
```

(Also see the discussion of whether to break before or after binary operators below.)

The closing brace/bracket/parenthesis on multiline constructs may either line up under the first non-whitespace charcater of the last line of list, as in:

```python
my_list = [
	1, 2, 3,
	4, 5, 6,
	]
result = some_function_that_takes_arguments(
	'a', 'b', 'c',
	'd', 'e', 'f',
	)
```

or it may be lined up under the first character of the line that starts the multiline construct, as in:

```python
my_list = [
	1, 2, 3,
	4, 5, 6,
]
result = some_function_that_takes_arguments(
	'a', 'b', 'c',
	'd', 'e', 'f',
)
```

## Naming Conventions

The naming conventions of Python's library are a bit of a mess, so we'll never get this completely consistent - nevertheless, here are the currently recommended naming standards. New modules and packages (including third party frameworks) should be written to these standards, but where an existing library has a different style, internal consistency is preferred.

### Descriptive: Naming Styles

There are a lot different naming styles. It helps to be able to recognize what naming style is being used, independently from what they are used for.

The following naming styles are commonly distinguished:

- `b` (single lowercase letter)

- `B` (single uppercase letter)

- `lowercase`

- `lower_case_with_underscores`

- `UPPERCASE`

- `UPPER_CASE_WITH_UNDERSCORES`

- `CapitalizedWords` (or CapWords, or CamelCase - so named because of the bumpy look of its letters). This is also sometimes known as StudlyCaps.

Note: When using acronyms in CapWords, capitalize all the lettes of the acronym. Thus HTTPServerError is better than HttpServerError.

- `mixedCase` (differs from CapitizedWords by initial lowercase character!)

- `Capitalized_Words_With_Underscores` (ugly!)

There's also the style of using a short unique prefix to group related names together. This is not used much in Python, but it is mentioned for completeness. For example, the `os.stat()` function returns a tuple whose items traditionally have names like `st_mode`, `st_size`, `st_mtime` and so on. (This is done to emphasize the correspondence with the fields of the POSIX system call struct, which helps programmers familiar with that.)

The X11 library uses a leading X for all its publics functions. In Python, this style is generally deemed unnecessary because attribute and method names are prefixed with an object, and function names are prefixed with a module name.

In addition, the following special forms using leading or trailing underscore are recognized (these can generally be combined with any case convention):

- `_single_leading_underscore`: weak "internal use" indicator. E.g. `from M import *` does not import objects whose names start with an underscore.

- `single_trailing_underscore_`: used by convention to avoid conflicts with Python keyword, e.g.

```python
tkinter.Toplevel(master, class_='ClassName')
```

- `__double_leading_underscore`: when naming a class attribute, invokes name mangling (inside class FooBar, `__boo` becomes `_FooBar__boo`; see below).

- `__double_leading_and_trailing_underscore__`: "magic" objects or attributes that live in user-controlled namespaces. E.g. `__init__`, `__import__` or `__file__`. Never invent such names; only use them as documented.

https://peps.python.org/pep-0008
