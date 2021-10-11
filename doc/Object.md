# Core [[Budd/Object|Object]]
#ST #Python 

In the simplest case, we only wrap any Python type into the base `Object` class:

```py
## core object
class Object:
    def __init__(self, V):
        self.value = V
```

Also, we need to display any object in a human-readable form. For tests, we need to do dumps reproducible between test runs, so some elements from dumps must be hidden.

```py
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
```

For [[ST/Primitive|Primitive]] types dumps can be simple: only short header which show type and value for the selected object in the `<tag:value>` printable form. Any dump starts from the new line to make multiple sequential dumps more readable.

```py
def test_nil():
    assert Nil().test() == '\n<nil:>'
def test_integer():
    assert Int(12.34).test() == '\n<int:12>'
```

The more complex objects will include extra elements which will interest us in debugging. Any nested object can in turn be complex, or reference objects in a higher level of nesting (references can form directed cycles). Of cause, nested dumps are mostly important for [[Container]] data types such as lists, maps, and any other **oriented object graph**s which are *the core concept for program and data representation in our system*.

## next: [[Object graph]]
