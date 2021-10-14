## @file
## @brief meta: Smalltalk-like guest OS

from metaL import *

p = Project(
    title='''Smalltalk-like guest OS''',
    about='''
inspired by
[lawson]
	Lawson English
	[**Squeak from the very start**](https://www.youtube.com/playlist?list=PL6601A198DF14788D)
	impressive playlist: intro to the Smalltalk programming which gives its feel like a live working environment (look especially on debugging and the Morphic GUI)
''') \
    | Python() \
    | WX() \
    | ST()

p.sync()
