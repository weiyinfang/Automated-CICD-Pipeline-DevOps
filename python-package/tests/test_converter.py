"""Unit tests for tempconv.converter."""

import pytest
from tempconv import converter


def test_celsius_to_fahrenheit():
    """Freezing and boiling points convert correctly."""
    assert converter.celsius_to_fahrenheit(0) == 32
    assert converter.celsius_to_fahrenheit(100) == 212


def test_celsius_to_fahrenheit_wrong_input():
    """A non-numeric input raises TypeError."""
    with pytest.raises(TypeError):
        converter.celsius_to_fahrenheit("wrong input")


def test_fahrenheit_to_celsius():
    """Freezing and boiling points convert correctly."""
    assert converter.fahrenheit_to_celsius(32) == 0
    assert converter.fahrenheit_to_celsius(212) == 100


def test_fahrenheit_to_celsius_wrong_input():
    """A non-numeric input raises TypeError."""
    with pytest.raises(TypeError):
        converter.fahrenheit_to_celsius("wrong input")


def test_celsius_to_kelvin():
    """0 °C is 273.15 K."""
    assert converter.celsius_to_kelvin(0) == pytest.approx(273.15)


def test_celsius_to_kelvin_wrong_input():
    """A non-numeric input raises TypeError."""
    with pytest.raises(TypeError):
        converter.celsius_to_kelvin("wrong input")
