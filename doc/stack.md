# stack operations
#ST #Py

## add / get / remove

```py
    ## `( -- o )`
    def push(self, that): return self // Object.box(that)
```
```py
    ## `( o1 o2 -- o1 )`
    def pop(self, idx=-1): return self.nest.pop(idx)
```
```py
    ## `( o -- o )`
    def top(self, idx=-1): return self.nest[idx]
```

## reorder

```py
    ## `( o - o o )`
    def dup(self): return self // self.top()
```
```py
    ## `( o1 o2 -- o1 )`
    def drop(self): self.pop(); return self
```
```py
    ## `( o1 o2 -- o2 o1 )`
    def swap(self): return self // self.pop(-2)
```
```py
    ## `( o1 o2 -- o1 o2 o1 )`
    def over(self): return self // self.top(-2)
```
