import translator
import pytest

# Test for null input for frenchToEnglish
def englishToFrench():
    assert translator.englishToFrench(None) == None

# Test for null input for englishToFrench.
def frenchToEnglish():
    assert translator.frenchToEnglish(None) == None

# Test for the translation of the world 'Hello' and 'Bonjour'.
def test_hello():
    assert translator.englishToFrench("Hello") == "Bonjour"

# Test for the translation of the world 'Bonjour' and 'Hello'.
def test_bonjour():
    assert translator.frenchToEnglish("Bonjour") == "Hello"

# Run these tests with `python3 -m pytest tests.py`