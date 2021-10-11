# compiler
#ST #VM

Source code methods written by programmers are translated by a [[ST/compiler]] into sequences of eight-bit instructions called [[bytecode]]s. Also, the [[ST/compiler]] is implemented as a runtime library, and available to the user, so some code can work directly with bytecode. So, you can do some magic in runtime, such as custom syntax compilers, optimizers, and low-level code generation.

Source methods written by programmers are represented in the Smalltalk-80 system as instances of multiline [[String]]s. This [[String]]s contain sequences of characters that conform to the ST [[syntax]]. For example, the following source method might describe how instances of class [[Rectangle]] respond to the unary message `center`. The `center` message is used to find the [[Point]] equidistant from a [[Rectangle]]'s four sides:

```smalltalk
center

^ origin + corner / 2
```

