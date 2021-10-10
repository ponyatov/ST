## @file
## @brief Smalltalk-like guest OS
## @defgroup Budd
## @brief Smalltalk-like guest OS
## @{

import config
import os, sys

## core object
class Object:
    def __init__(self, V):
        self.value = V

    def test(self): return self.dump(test=True)
    def __repr__(self): return self.dump()

    def dump(self, cycle=[], depth=0, prefix='', test=False):
        # head
        def pad(depth): return '\n' + '\t' * depth
        ret = pad(depth) + self.head(prefix, test)
        # subtree
        return ret

    def head(self, prefix='', test=False):
        gid = f' @{id(self):x}' if not test else ''
        return f'{prefix}<{self.tag()}:{self.val()}>{gid}'

    def tag(self): return self.__class__.__name__.lower()
    def val(self): return f'{self.value}'


## system init
if __name__ == '__main__':
    pass

## @}
