Code Unto Others
================

* https://us.pycon.org/2016/schedule/presentation/2075/
* Nathaniel Manista (gRPC), Augie Fackler (Mercurial)

The `localrepository` class in Mercurial
----------------------------------------
Software is Made of People

Readability - your software needs to describe itself to readers the way you
would describe it

Lack of cohesion - lowers readability

Mixes function and convenience

Mixes layers of abstraction: has low-level structures and high-level structures
that use those low-level structures

Too many elements in its API (> 100 for developers, > 50 for consumers)
* does this and that and this (and, and, and)

Text is too long. (1700+ lines!)

Requirements of any software change:
* a change must meet a need in the domain of the software
* the author must understand the ... (?)

We tend to underestimate the lifetime of our code

If it's apparent where the state is changed and how program control is passed
from one component to another, the code is much easier to understand,
regardless of the problem domain.

*Code* where the *coding* is simplest.

Put everything in module scope, unless it really needs to be part of the class.
(Would it be broken without that piece of data?)

Don't abuse classes.

Designing Classes
-----------------
Avoid self-use of public APIs.

Avoid self-escape in class implementation; pass something less than `self`.

Minimize instance state, especially outside of `__init__`.

Modules
-------

Always place imports at the top of your modules. Avoid circular imports.

Import reference modules, even if you don't directly need it. Can be nice
to type-checking helpers.

Default to private visibility, then promote to public as necessary.

Line limits and complexity limits on functions, classes, and modules, are good.

What makes conforming to line limits hard? Intellectual laziness - if it's
really about the public API, split out the intermediate parts. Intermediate
concepts are abstractions that help you understand things better later, even
if it seems obvious at the time.

Don't abbreviate when naming - especially if you're making up the abbreviation.

Sort your code elements in definition-before-use order.
* this has the effect of pushing public parts of your code down to the bottom
* but maintainers of your code need to be there anyway, and users should
have docs to read

Code unto Others
----------------
Readability is independent of correctness, efficiency, and problem domain
* classes invite questions and complexity
* consider setting aside your own judgements
* when forced to choose between favoring writing for users or maintainers,
choose your maintainers
