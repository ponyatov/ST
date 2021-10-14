# operators
#ST #Py #operator

Operators let to modify and build objects graphs using Python literals in a code and give a better readable Python code that manipulates object graphs. With Python magic, we can redefine some operators for the [[Object]] and all inherited classes:

```py
class Object:
    ## `A.keys()` get slot names in order
    def keys(self): return sorted(self.slot.keys())
```
```py
    ## `iter(A)` iterate over nest[]ed
    def __iter__(self): return iter(self.nest)
```
```py
    ## `len(A)`
    def __len__(self): return len(self.nest)
```

`.keys()` and `.iter()` methods are required for `dump()` because they are used as *group addressing operators*: iterate over slot names, and over nested elements respectively.

```py
    ## type/class tag
    def tag(self): return self.__class__.__name__.lower()
```
```py
    ## value represented for dumps
    def val(self): return f'{self.value}'
```

Also, `tag`/`val` must be moved to operators, because they are used as some sort of address-generator operators: any object has the class name and sometimes object value; both of them can be used as addresses if this object was stored somewhere as a subgraph element (see next).

```py
    ## `A // B -> A.append(B)` append to end of A
    def __floordiv__(self, that):
        that = Object.box(that)
        self.nest.append(that); return self
```

The most used operation is adding a new nested object or subgraph.

```py
    ## `A[key]` get slot by name, or nested element by integer index
    def __getitem__(self, key):
        if isinstance(key, str): return self.slot[key]
        if isinstance(key, int): return self.nest[key]
        assert TypeError(['__getitem__', type(key), key])
```
```py
    ## `A[key] = B` set slot by name
    def __setitem__(self, key, that):
        assert isinstance(key, str)
        that = Object.box(that)
        self.slot[key] = that; return self
```

The fetch/store operations are available thru list-like indexing:
- slots addressed by strings
- nested elements available via an integer index
- Python has no native sparse lists, so assignments can be done only for slots

```py
    ## `A << B -> A[B.tag] = B` assign slot by B class tag
    def __lshift__(self, that):
        that = Object.box(that)
        return self.__setitem__(that.tag(), that)
```
```py
    ## `A >> B -> A[B.val] = B` assign slot by B value
    def __rshift__(self, that):
        that = Object.box(that)
        return self.__setitem__(that.val(), that)
```


`<<` and `>>` **shift operations** are frequently used when you build some descriptional or HTML-like data structure with attribute names generated from objects assigned to its slots:

```py
## Video Graphics Array
class VGA(HW): pass
class Mode(VGA): pass
class Color(VGA): pass

vga = VGA('text') << Mode('80x25') >> Color('blue')
```
```
<vga:text> @7f672e2df780
    blue = <color:blue> @7f672e2dfe10
    mode = <mode:80x25> @7f672e2df978
```

<hr>
With these operators we can rewrite the `Object.dump()` method, to make the full object graph [[ST/dump|dump]].

Next, we can also define [[stack]] operations.
