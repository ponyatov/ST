from ST import *
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

def test_map_empty():
    assert Map().test() == '\n<map:>'

def test_vector_empty():
    assert Vector().test() == '\n<vector:>'

def test_stack_empty():
    assert Stack().test() == '\n<stack:>'

def test_queue_empty():
    assert Queue().test() == '\n<queue:>'

def test_box_object():
    assert Object.box(Object('')).test() == '\n<object:>'

def test_box_nil():
    assert Object.box(None).test() == '\n<nil:>'

def test_box_str():
    assert Object.box('abc').test() == '\n<str:abc>'

def test_box_int():
    assert Object.box(12).test() == '\n<int:12>'

def test_box_num():
    assert Object.box(34.56).test() == '\n<num:34.56>'

def test_box_keys():
    assert Object('').keys() == []

def test_box_iter():
    for i in iter(Object('')): pass
