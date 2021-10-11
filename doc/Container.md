# `Container` types
#ST #Python

Generalized container with variable size data storage

```py
## generic data container
class Container(Object):
    ## @param V unnamed by default
    def __init__(self, V=''):
        super().__init__(V)
```

## `Map`

Associative array works as a dictionary (and Forth vocabulary): store object with name, and return it by the same name.

```py
## associative array (dict, vocabulary)
class Map(Container):
    def __init__(self, V=''):
        super().__init__(V)
        ## attribute slot{}s
        self.slot = {}
```

## `Vector`

Ordered container

```py
## ordered container
class Vector(Container):
    def __init__(self, V=''):
        super().__init__(V)
        ## nest[]ed data
        self.nest = []
```

## `Stack`

Container which stores and retrieves data with Last-In-First-Out order

```py
## FIFO stack
class Stack(Vector): pass
```

## `Queue`

Object queue with Fist-In-First-Out discipline

```py
## FIFO queue
class Queue(Vector): pass
```

## [[Object graph]]

Here we should note some repeatable pattern which repeats not only for data containers but factically for all objects in a system -- we can generalize this pattern into the [[Object graph|directed object graph]] concept.
