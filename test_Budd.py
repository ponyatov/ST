from Budd import *
import pytest

def test_any(): assert True

def test_hello():
    assert Object('Hello').test() == '\n<object:Hello>'
