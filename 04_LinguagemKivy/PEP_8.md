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
def lon_function_name(
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

https://peps.python.org/pep-0008
