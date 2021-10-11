# `Primitive` types
#ST #Python

Some types can be represented at a machine level as integer and float numbers. While it is mostly a single number that encodes some scalar data element, **in Smalltalk anything is an object**, so primitives also can have some arbitrary properties such as measurement units or tolerance.

```py
## scalar data close to machine primitives
class Primitive(Object): pass
```

In most languages, there is some special type that represents "nothing" or an empty data container. For the first look, these two cases must be differentiated, here we touch some algebraic complexity with programming language concepts:
- can nothing, an empty list, and a reference to a non-existing object be the same or not?
- is "nothing" able to have some name?
- can we differ two nothings as separate objects, or all "nothing"s in a system must be the same global singleton object?

```py
## nothing
class Nil(Primitive):
    def __init__(self): super().__init__('')
```

- What is a number? How does it differ in math, and in computers?
- Should we treat floating-point numbers abstractly which is not true because computer numbers always has fixed range and precision?
- *Number as objects allow us to hold real measurements with units, precision, allowed range, and tolerance*. Should we use them in computations, and how it will increase the complexity of our language?

```py
## floating point
class Num(Primitive):
    def __init__(self, F): Primitive.__init__(self, float(F))
```

- are integers subclassed from floating-point numbers, or must have an independent inheritance?
- how can we manage it, if the implementation language does not support multiple inheritance like Java?
- how we should consider conversion in the case of constructing an integer from 12.34?

```py
class Int(Num):
    def __init__(self, N): Primitive.__init__(self, int(N))
```
- do we need hex and binary numbers, if we have no plans to work with hardware, drivers, or firmware coding?
- are hex/bin numbers special classes or it is just an integer written in a special form?
- how can we speak about machine number width in bits?
- what standard should we follow in number literals writing? is it allowed to use a digit separator In thousands?
- what prefix to use with hex: widely used `0x`, old-fashioned `16r` used only in Smalltalk, or Pascal-inspired `$`?
- should we expand numeric types more such as complex numbers, fractions, or bigints?

```py
class Str(Primitive): pass
```

- strings -- the topmost hell in computing...
- do we need single chars? how to group?.. list or vector?..
- slices... mutability... Unicode and encoding hell...
- are strings scalars or we can treat them as tree-like structures as we plan to work a lot with source code?

