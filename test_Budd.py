from Budd import *
import pytest

def test_any(): assert True

def test_hello():
    assert Object('Hello').test() == '\n<object:Hello>'

def test_nil():
    assert Nil().test() == '\n<nil:>'

def test_float():
    assert Num('3.1415').test() == '\n<num:3.1415>'

def test_integer():
    assert Int(12.34).test() == '\n<int:12>'

def test_string():
    assert Str('asdf').test() == '\n<str:asdf>'
