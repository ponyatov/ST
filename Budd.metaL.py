## @file
## @brief meta: Smalltalk-like guest OS

from metaL import *

p = Project(
    title='''Smalltalk-like guest OS''',
    about='''
* inspired by
  A Little Smalltalk (c) Timothy Budd
''') \
    | Python() \
    | ST()

p.sync()
