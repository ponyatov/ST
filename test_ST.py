from ST import *
import pytest

def test_any(): assert True


class TestPrimitive:

    def test_nil(self):
        assert Nil().test() == '\n<nil:>'

    def test_float(self):
        assert Num('3.1415').test() == '\n<num:3.1415>'

    def test_integer(self):
        assert Int(12.34).test() == '\n<int:12>'

    def test_string(self):
        assert Str('asdf').test() == '\n<str:asdf>'


class TestContainer:

    def test_map_empty(self):
        assert Map().test() == '\n<map:>'

    def test_vector_empty(self):
        assert Vector().test() == '\n<vector:>'

    def test_stack_empty(self):
        assert Stack().test() == '\n<stack:>'

    def test_queue_empty(self):
        assert Queue().test() == '\n<queue:>'


class TestBoxing():

    def test_object(self):
        assert Object.box(Object('')).test() == '\n<object:>'

    def test_nil(self):
        assert Object.box(None).test() == '\n<nil:>'

    def test_str(self):
        assert Object.box('abc').test() == '\n<str:abc>'

    def test_int(self):
        assert Object.box(12).test() == '\n<int:12>'

    def test_num(self):
        assert Object.box(34.56).test() == '\n<num:34.56>'


## basic operators
class TestHello:
    @pytest.fixture
    def fixture(self):
        self.hello = Object('Hello')
        self.world = Object('World')
        self.left = Object('left')
        self.right = Object('right')

    @pytest.fixture
    def fixhello(self, fixture):
        (self.hello // self.world) \
            << self.left \
            >> self.right

    def test_keys(self, fixhello):
        assert self.hello.keys() == \
            ['object', 'right']

    def test_iter(self, fixhello):
        t = iter(self.hello)
        assert next(t).test() == '\n<object:World>'
        with pytest.raises(StopIteration): next(t)

    def test_len(self, fixhello):
        assert len(self.hello) == 1

    def test_hello(self, fixture):
        assert self.hello.test() == \
            '\n<object:Hello>'

    def test_world(self, fixture):
        assert self.world.test() == \
            '\n<object:World>'
        assert (self.hello // self.world).test() == \
            '\n<object:Hello>' +\
            '\n\t0: <object:World>'

    def test_op_shifts(self, fixhello):
        assert self.hello.test() == \
            '\n<object:Hello>' +\
            '\n\tobject = <object:left>' +\
            '\n\tright = <object:right>' +\
            '\n\t0: <object:World>'


class TestStack:
    @pytest.fixture
    def fixture(self):
        self.stack = Stack() // 1 // 2

    def test_goodstack(self, fixture):
        assert self.stack.test() == \
            '\n<stack:>' +\
            '\n\t0: <int:1>' +\
            '\n\t1: <int:2>'

    def test_push(self, fixture):
        assert self.stack.push(3).test() == \
            '\n<stack:>' +\
            '\n\t0: <int:1>' +\
            '\n\t1: <int:2>' +\
            '\n\t2: <int:3>'

    def test_pop(self, fixture):
        assert self.stack.pop().test() == \
            '\n<int:2>'

    def test_top(self, fixture):
        assert self.stack.top().test() == \
            '\n<int:2>'

    def test_dup(self, fixture):
        assert self.stack.dup().test() == \
            '\n<stack:>' +\
            '\n\t0: <int:1>' +\
            '\n\t1: <int:2>' +\
            '\n\t2: <int:2> _/'

    def test_drop(self, fixture):
        assert self.stack.drop().test() == \
            '\n<stack:>' +\
            '\n\t0: <int:1>'

    def test_swap(self, fixture):
        assert self.stack.swap().test() == \
            '\n<stack:>' +\
            '\n\t0: <int:2>' +\
            '\n\t1: <int:1>'

    def test_over(self, fixture):
        assert self.stack.over().test() == \
            '\n<stack:>' +\
            '\n\t0: <int:1>' +\
            '\n\t1: <int:2>' +\
            '\n\t2: <int:1> _/'


class TestGUI:
    def test_preinit(self):
        assert gui.test() == \
            '\n<gui:wx>'
