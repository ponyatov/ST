# operators
#ST #Py

Operators let to modify and build objects graphs using Python literals in a code and give a better readable Python code that manipulates object graphs. With Python magic, we can redefine some operators for the [[Object]] and all inherited classes:

```py
class Object:
    ## get slot names in order
    def keys(self): return sorted(self.slot.keys())
```
```py
    ## iterate over nest[]ed
    def __iter__(self): return iter(self.nest)
```

With these operators we can rewrite the `Object.dump()` method, to make the full object graph [[ST/dump|dump]]s.
