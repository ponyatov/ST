# Object graph
#ST #Py

As you can note in [[Container]] classes, there is a specific pattern that also repeats almost in all data types: 
- every object in a system can have **arbitrary attributes**, so 
	- any object can be treated as a [[Map]]
- every object should be able to **hold some data in order**, so 
	- any object can be treated as a [[Vector]]

If you read something about programming language design, in the first chapter of any textbook about compilers you can find two tightly coupled concepts:
- [[AST]] is about represeting source code for any programming language
- [[attribute grammar]] extends AST with
	- attributes can be assigned for every program tree node, and
	- ability to do computations over them.

The *directed object graph* (1)
- is much more powerful and has higher abstraction level then AST (2)
- **object graph is an universal data structure** for any data, and
	- especially for program code as an internal program representation (3);
	- so we can speak about the [[homoiconicity]]: the *must-have property for any programming system we want to be interactive and dynamic*
- if you work in the AI domain or knowledge-based programming, you can directly link object graph concept with [Marvin Minsky's Frames](https://web.media.mit.edu/~minsky/papers/Frames/frames.html) as a universal knowledge representation

<hr>
(1) formed by objects and links between them as references/pointers to other objects

(2) or Lisp lists

(3) programs can be written directly as data structures in memory (4), without the use of any text code in files or string fragments, but it is incompatible with mainstream habits and the git use for code sharing

(4) working memory of ST system can be mapped to swap-like files for data storage and persistence, which maked the ST system some sort of object database
<hr>

 Returning to [[Container]] classes, we can generalize some of their behavior to the core [[Object]] class, and see on them just as a special use case of any object.
 
 ```py
 ## core object
class Object:
    def __init__(self, V):
        ## scalar: object name, string/number value,..
        self.value = V
        ## associative array: map = env/namespace
        self.slot  = {}
        ## ordered container: vector = stack = queue = AST
        self.nest  = []
```
```py
class Container(Object):
    ## @param V unnamed by default
    def __init__(self, V=''): super().__init__(V)

class Map(Container): pass
class Vector(Container): pass
class Stack(Vector): pass
class Queue(Vector): pass
```
