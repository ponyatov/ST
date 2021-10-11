# Classical Smalltalk drawbacks
#ST

## hurdy syntax:

- the lack of data containers at the core language syntax (tuple, list, map)
- modern programmers prefer Algolic, C-like, or Pythonic syntax and don't like press colons in the assignment operator
- **programming language targets on fast software [[prototyping]]** should be user-expandable and allow to define/modify custom syntax and enhance compiler with power macroses

## image-based engine

Modern programming requires systems based on files due to the requirement of `git` usage at least for system snapshots and library sharings. Classical ST uses cranky images which are not suitable for real and massive use.

## pure interpreter nature