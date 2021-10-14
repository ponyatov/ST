# full object graph `dump()`
#ST #PY #dump

With these [[operators]] we can rewrite the `Object.dump()` method, to make the full object graph [[dump]]s.

```py
class Object:
    ## full text tree dump
    def dump(self, cycle=[], depth=0, prefix='', test=False):
        # header
        def pad(depth): return '\n' + '\t' * depth
        ret = pad(depth) + self.head(prefix, test)
        # cycle break
        if not depth: cycle = [] # init
        if self in cycle: return f'{ret} _/'
        else: cycle.append(self)
        # slot{}s
        for i in self.keys():
            ret += self[i].dump(cycle, depth + 1, f'{i} = ', test)
        # nest[]editor
        for j, k in enumerate(self):
            ret += k.dump(cycle, depth + 1, f'{j}: ', test)
        # subtree
        return ret
```

## tree dump

To dump (hyper)graph in a human-readable form (and for tests) we can use tree-like text dump: padding shows how deep we are from the starting graph node.

The `<T:V>` header shows the most important info on every object: its type, and name or value.

Next, we output all object attributes a.k.a. **slot**s, in a form: `name = <sub-dump>`. All slot names are outputs in a sorted order via the `keys()` method, which lets us easily find the slot which we want to study.

Finally, all nested subgraph should be dumped in order with their position index. When you want to treat some object in a stack matter, the stack top will be the downside as stacks frequently grow top to down (as hardware x86 stacks do for example).

## cycle breaking

The **[[object graph]] is a cyclic self-referencing data structure**, so when dump recursion goes deeper and deeper in the graph it falls into an infinity loop.

So, in the `dump()` method we have a special code section and the `cycle` parameter which accumulates all already dumped hypergraph nodes. Every next node should be checked is it already dumped, and recursion breaks with `_/` marker added to the node header.

Accumulator must be passed with every consequent recursion call, which you can see in `slot{}` and `nest[]` dumping code. In the root of recursion, when you start to dump, the `depth` parameter has a zero recursion depth value, and here we must preinitiate the cycle parameter with an empty list.

