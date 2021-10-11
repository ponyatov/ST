# Implementation
## Simplicity over Completeness
#ST #Budd 

This Smalltalk-ish language variant is far from its original design.

First of all, the origin ST is significantly overcomplicated, which is not good both for learning, modifications, or porting to new systems. It is not a good idea also to follow old language design decisions which showed itself non-compatible with modern programming habits and limit the system use in integration with already existing infrastructure.

So an unpopular decision was taken to follow the spirit of the Smalltalk, but not its syntax and standards:
- active object storage engine
	- some sort of object database (still in RAM but who knows...)
- more pythonic syntax
	- base data containers as literals
	- infix operators with overloading
- ASCII files snapshots and source code loading for
	- git-based libraries sharing and managing
- implementation adapted for script engine embedding
	- more high-level interpreter model
	- rely on the host language's built-in memory management mechanisms (as it is possible)

## Two host (implementation) languages were selected:

- [[Budd/Python|Python]] very popular and easy to use
- [[Budd/Rust|Rust]] perspective low-level language solves a lot of problems of the classical C/C++ (not very popular now but has a good potential)

## Simplicity over Completeness

For the language that targets programming learning, it is important to be easier to learn it and especially to understand its concepts and paradigm.

For experimental language wants to survive among dozens of modern mature programming languages, it is most important to be as simple as possible in its implementation -- it lets to attract new programmers who want to understand some language internals, and to make their own custom version.

As an example, we can point to the Forth language -- it is still alive despite its very high level of esotericism and extra low-levelness. We'll even use it for control and debug, until our ST will not start to breathe itself. **The key is the internal Simplicity.** When people want to learn programming they cry and run away from the Forth when first time looks at it. But, when some programmer becomes more or less mature and wants to touch programming languages design itself, the Forth becomes so attractive for the start because it is so simple. Any newbie programmer is able to understand its internals just while reading a textbook, and saying more, to write some own working variant in a few days or weeks.

As a result, the Forth language still stays alive does not matter how it is scary in real use. In contrast, it does not matter how Smalltalk is friendly and magic but it died in 90th -- because your brain explodes while you are reading [budd] or the [bluebook] in a few first times.
