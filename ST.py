## @file
## @brief Smalltalk-like guest OS
## @defgroup ST
## @brief Smalltalk-like guest OS
## @{

import config
import os, sys

## core object
class Object:
    def __init__(self, V):
        ## scalar: object name, string/number value,..
        self.value = V
        ## associative array: map = env/namespace
        self.slot = {}
        ## ordered container: vector = stack = queue = AST
        self.nest = []

    ## Python types wrapper
    def box(that):
        if isinstance(that, Object): return that
        if that is None: return Nil()
        if isinstance(that, str): return Str(that)
        if isinstance(that, int): return Int(that)
        if isinstance(that, float): return Num(that)
        raise TypeError(['box', type(that), that])

    ## @name dump

    ## `pytest` callback
    def test(self): return self.dump(test=True)

    ## `print` callback
    def __repr__(self): return self.dump()

    ## full text tree dump
    def dump(self, cycle=[], depth=0, prefix='', test=False):
        # header
        def pad(depth): return '\n' + '\t' * depth
        ret = pad(depth) + self.head(prefix, test)
        # cycle break
        if not depth: cycle = [] # init
        if self in cycle: return f'{ret} _/'
        else: cycle.append(self)
        # slot{}s
        for i in self.keys():
            ret += self[i].dump(cycle, depth + 1, f'{i} = ', test)
        # nest[]editor
        for j, k in enumerate(self):
            ret += k.dump(cycle, depth + 1, f'{j}: ', test)
        # subtree
        return ret

    ## `<T:V>` header
    def head(self, prefix='', test=False):
        gid = f' @{id(self):x}' if not test else ''
        return f'{prefix}<{self.tag()}:{self.val()}>{gid}'

    ## @name operator

    ## `A.keys()` get slot names in order
    def keys(self): return sorted(self.slot.keys())

    ## `iter(A)` iterate over nest[]ed
    def __iter__(self): return iter(self.nest)

    ## `len(A)`
    def __len__(self): return len(self.nest)

    ## type/class tag
    def tag(self): return self.__class__.__name__.lower()

    ## value represented for dumps
    def val(self): return f'{self.value}'

    ## `A // B -> A.append(B)` append to end of A
    def __floordiv__(self, that):
        that = Object.box(that)
        self.nest.append(that); return self

    ## `A[key]` get slot by name, or nested element by integer index
    def __getitem__(self, key):
        if isinstance(key, str): return self.slot[key]
        if isinstance(key, int): return self.nest[key]
        assert TypeError(['__getitem__', type(key), key])

    ## `A[key] = B` set slot by name
    def __setitem__(self, key, that):
        assert isinstance(key, str)
        that = Object.box(that)
        self.slot[key] = that; return self

    ## `A << B -> A[B.tag] = B` assign slot by B class tag
    def __lshift__(self, that):
        that = Object.box(that)
        return self.__setitem__(that.tag(), that)

    ## `A >> B -> A[B.val] = B` assign slot by B value
    def __rshift__(self, that):
        that = Object.box(that)
        return self.__setitem__(that.val(), that)

    ## @name stack

    ## `( -- o )`
    def push(self, that): return self // Object.box(that)

    ## `( o1 o2 -- o1 )`
    def pop(self, idx=-1): return self.nest.pop(idx)

    ## `( o -- o )`
    def top(self, idx=-1): return self.nest[idx]

    ## `( o - o o )`
    def dup(self): return self // self.top()

    ## `( o1 o2 -- o1 )`
    def drop(self): self.pop(); return self

    ## `( o1 o2 -- o2 o1 )`
    def swap(self): return self // self.pop(-2)

    ## `( o1 o2 -- o1 o2 o1 )`
    def over(self): return self // self.top(-2)


## scalar data close to machine primitives
class Primitive(Object): pass

## nothing
class Nil(Primitive):
    def __init__(self): super().__init__('')

## floating point
class Num(Primitive):
    def __init__(self, F): Primitive.__init__(self, float(F))

class Int(Num):
    def __init__(self, N): Primitive.__init__(self, int(N))

class Str(Primitive): pass


## generic data container
class Container(Object):
    ## @param V unnamed by default
    def __init__(self, V=''): super().__init__(V)

## associative array (dict, vocabulary)
class Map(Container): pass

## ordered container
class Vector(Container): pass

## LIFO stack
class Stack(Vector): pass

## FIFO queue
class Queue(Vector): pass


## hardware components
class HW(Object): pass

## Video Graphics Array
class VGA(HW): pass
class Mode(VGA): pass
class Color(VGA): pass

vga = VGA('text') << Mode('80x25') >> Color('blue')


class GUI(Object): pass

gui = GUI('wx')

class Screen(GUI):
    def __init__(self, V=''):
        self.wx = __import__('wx')


## external API
class API(Object): pass

## vk.com API (well known Russian social network)
## @details https://pythonrepo.com/repo/python273-vk_api-python-third-party-apis-wrappers
class VK(API):
    def __init__(self, V='api'):
        super().__init__(V)
        self.api = __import__('vk_api')

## system init
if __name__ == '__main__':
    pass
    # vk = VK(); print(vk)

## @}
