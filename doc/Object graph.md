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
	- especially for program code;
	- so we can speak about the [[homoiconicity]]: the *must-have property for any programming system we want to be interactive and dynamic*

(1) formed by objects and links between them as references/pointers to other objects
(2) or Lisp lists