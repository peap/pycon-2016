Removing Python's GIL: The Gilectomy
====================================

* https://us.pycon.org/2016/schedule/presentation/2101/
* github.com/larryhastings/gilectomy
* #gilectomy
* Larry Hastings

GIL was added in 1992 to protect global/static variables in CPython when
threading was being added to operating systems.

GIL Ramifications:
* simple
 * easy to get right
 * no deadlocks (only one lock)
* low overhead
* single-threaded code is fast!
* if you're I/O bound, you're ok
* if you're CPU-bound, you're out of luck - you're single-threaded

Threading and multi-core is much more important now, but Python is
still best for single cores.

There was a previous removal of the GIL in Python 1.4 (1999). The
"free-threading" patch. Made code 4-7 times slower. The GIL helps python run
faster. (See David Beazley article from 2011.)

*Time to try again: the gilectomy.*

Four technical considerations:
* reference counting
* globals & statics
 * per-thread
 * shared singletons
* C extension parallelism and reentrancy
* atomicity

Three political considerations:
* don't hurt single-threaded performance
* don't break C extensions
* don't make it too complicated

Approaches
----------
Tracing Garbage Collection
* about as fast as reference counting, but...
* breaks C extensions
* complicated

Software Transactional Memory
* new and very complicated - hard to get it right
* great performance
* would break C extensions
* super complicated

Larry's Progress
----------------
Still using reference counting.

Atomic increment/decrement - costs about 30% speed.

Globals and statics: per-thread already (PyThreadState)

C extensions currently break, but... it'll be opt-in:
* `./configure -without-gil`
* different entry points for GIL/no-GIL builds of Python

Locks - millions of new, tiny locks! `Py_LOCK` and `Py_UNLOCK`. Have to lock
any mutable objects in *C*. For example:
* `str`
 * `hash` is computed lazily
 * `utf8` and `wstr` also get computed lazily

Need "userspace" locks - only use user-space code until there is contention
between locks that the kernel needs to resolve. `futex` in Linux.

This new API could present a good opportunity to enforce best practices.

Guido's blog post from 2007: It isn't easy to remove the GIL.

About 3.5x slower, wall time. About 25x slower, CPU time.
