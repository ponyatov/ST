from ST import *
import pytest

def test_any(): assert True

hello = Object('Hello')

def test_hello():
    assert hello.test() == '\n<object:Hello>'

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

world = Object('World')

def test_op_append():
    assert (hello // world).test() == \
        '\n<object:Hello>' +\
        '\n\t0: <object:World>'

left = Object('left')
right = Object('right')

def test_op_shifts():
    hello << left >> right
    assert hello.test() == \
        '\n<object:Hello>' +\
        '\n\tobject = <object:left>' +\
        '\n\tright = <object:right>' +\
        '\n\t0: <object:World>'

stack = Stack()

def test_stack_push():
    assert stack.test() == '\n<stack:>'
    stack.push(1) // 2
    assert stack.test() == \
        '\n<stack:>' +\
        '\n\t0: <int:1>' +\
        '\n\t1: <int:2>'

def test_stack_pop():
    assert stack.pop().test() == '\n<int:2>'
    assert stack.test() == \
        '\n<stack:>' +\
        '\n\t0: <int:1>'

def test_stack_top():
    assert stack.top().test() == '\n<int:1>'
    assert stack.test() == \
        '\n<stack:>' +\
        '\n\t0: <int:1>'

def test_stack_dup():
    assert stack.dup().test() == \
        '\n<stack:>' +\
        '\n\t0: <int:1>' +\
        '\n\t1: <int:1> _/'

def test_stack_drop():
    assert stack.drop().test() == \
        '\n<stack:>' +\
        '\n\t0: <int:1>'

def test_stack_swap():
    stack // 2
    assert stack.swap().test() ==\
        '\n<stack:>' +\
        '\n\t0: <int:2>' +\
        '\n\t1: <int:1>'

def test_stack_over():
    assert stack.over().test() ==\
        '\n<stack:>' +\
        '\n\t0: <int:2>' +\
        '\n\t1: <int:1>' +\
        '\n\t2: <int:2> _/'
