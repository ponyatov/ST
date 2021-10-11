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
        self.value = V

    ## @name dump

    ## `pytest` callback
    def test(self): return self.dump(test=True)

    ## `print` callback
    def __repr__(self): return self.dump()

    ## full text tree dump
    def dump(self, cycle=[], depth=0, prefix='', test=False):
        # head
        def pad(depth): return '\n' + '\t' * depth
        ret = pad(depth) + self.head(prefix, test)
        # subtree
        return ret

    ## `<T:V>` header
    def head(self, prefix='', test=False):
        gid = f' @{id(self):x}' if not test else ''
        return f'{prefix}<{self.tag()}:{self.val()}>{gid}'

    ## type/class tag
    def tag(self): return self.__class__.__name__.lower()

    ## value represented for dumps
    def val(self): return f'{self.value}'


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
    def __init__(self, V=''):
        super().__init__(V)

## associative array (dict, vocabulary)
class Map(Container):
    def __init__(self, V=''):
        super().__init__(V)
        ## attribute slot{}s
        self.slot = {}

## ordered container
class Vector(Container):
    def __init__(self, V=''):
        super().__init__(V)
        ## nest[]ed data
        self.nest = []

## LIFO stack
class Stack(Vector): pass

## FIFO queue
class Queue(Vector): pass

## system init
if __name__ == '__main__':
    pass

## @}
