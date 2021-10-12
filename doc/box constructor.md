# `box` constructor

Here we'll add a custom **box constructor** which wraps Python types into object graph nodes.

```py
class Object:
    ## Python types wrapper
    def box(that):
        if isinstance(that, Object): return that
        if that is None: return Nil()
        if isinstance(that, str): return Str(that)
        if isinstance(that, int): return Int(that)
        if isinstance(that, float): return Num(that)
        raise TypeError(['box', type(that), that])
```

Later, it will be used in [[operators]] which let to modify and build objects graphs using Python literals in a code.