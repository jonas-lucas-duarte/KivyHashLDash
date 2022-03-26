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

https://peps.python.org/pep-0008
