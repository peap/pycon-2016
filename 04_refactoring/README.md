Refactoring Python: Why and how to restructure your code
========================================================

* https://us.pycon.org/2016/schedule/presentation/2073/
* github.com/bslatkin/pycon2016
* Brett Slatkin
* onebigfluke.com

What is refactoring? Repeatedly reorganizing and rewriting code until it's
*obvious* to a new reader.

When do you refactor?
* in advance of new changes
* when you're going to write tests
* when you're copy/pasting a lot (DRY)
* when you find brittleness
* when you find it complex

Great programmers spend about half the time refactoring, stylizing and writing
docs up-front

How?
* identify bad code
* improve it
* run tests
* fix and improve tests
* repeat

In practice, what does it mean?
* rename, split and move arguments and functions
* simplify the code
* redraw class/module boundaries

Canonical reference: Refactoring by Martin Fowler
* really for Java, though
* (2009) another edition for Ruby

Strategies
----------
Three important strategies

Prerequisites
* thorough tests
* quick tests (< 5 minutes)
* source control
* willingness to make mistakes
 * get out of the "don't want to break it" mindset

### Extracting Variables

Extract variables: make it clearer what you're doing, no performance hit

Extract variables into functions

Using functions with variables: cache values, and add clarity to if-statements

As functions get more complicated, extract variables into classes that cache
results of computations, which are returned in `__bool__` or `__nonzero__`.

Using a class instead of a function makes it easier to test the computation -
you get access to any intermediate things.

### Extract class and move fields

Complicated classes that keep growing are ready to have their boundaries
refactored.

How do you redraw boundaries?
1. Add an improved interface
 * maintain backwards compatibility
 * issue warnings for old usage  (`import warnings; warnings.warn`)
2. Remove ... (?)

Move attributes for new interfaces into inner objects
* `pet.animal.has_scales` (instead of `pet.has_scales`)
* add warning for old-style usage (in a `property` method)

Things to remember:
* split classes using optional arguments to `__init__`
* use @property to move methods and attributes between classes
* ... (?)
* Need defensive property tombstones (to prevent usage of old attributes)
