# API reference

All functions live in the `tempconv.converter` module. They accept an `int`
or `float` and return a `float`. A string argument raises `TypeError`.

| Function | Formula |
|----------|---------|
| `celsius_to_fahrenheit(c)` | `c * 9/5 + 32` |
| `fahrenheit_to_celsius(f)` | `(f - 32) * 5/9` |
| `celsius_to_kelvin(c)` | `c + 273.15` |

## `celsius_to_fahrenheit(c)`

Convert Celsius to Fahrenheit.

```python
>>> celsius_to_fahrenheit(0)
32.0
>>> celsius_to_fahrenheit(100)
212.0
```

## `fahrenheit_to_celsius(f)`

Convert Fahrenheit to Celsius.

```python
>>> fahrenheit_to_celsius(32)
0.0
>>> fahrenheit_to_celsius(212)
100.0
```

## `celsius_to_kelvin(c)`

Convert Celsius to Kelvin.

```python
>>> celsius_to_kelvin(0)
273.15
```

## Errors

```python
>>> celsius_to_kelvin("hot")
Traceback (most recent call last):
  ...
TypeError: can only concatenate str (not "float") to str
```
