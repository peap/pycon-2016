Thinking in Coroutines
======================

* https://us.pycon.org/2016/schedule/presentation/1801/
* fb.me/coroutines
* Łukasz Langa
* @llanga
* fb.me/ambv

Why do async?
-------------

`yield from` showed possibility for nice async syntax, like twisted
had been doing.

What is asyncio?
----------------

* event loop with callbacks
* maximize usage of a single thread
* keep our CPU busy

With `PYTHONASYNCIODEBUG=1`, python will warn about long-running callbacks.

What's included?
----------------
asyncio provides a lot of things: locks, queues, network calls, file access

aiohttp - high-level, async HTTP

uvloop - high-speed looping

What about third-party, blocking code? executors!
* ThreadPoolExecutor (GIL, less overhead)
* ProcessPoolExecutor (No GIL, picklable arguments only)

Asyncio at Facebook: 100k lines of asyncio code (33k at Instagram)

Make sure to have the kernel kill child processes if the parent dies
(some ctypes code shown in slides)

Random Advice
-------------
* Use Python 3.5+.
* Write unit tests
 * easy to mock out coroutines
* Set up debugging
* Do *not* use `StopIteration`
 * in Python 3, you can return from a generator, instead
* Read the docs, and the asyncio source (it's a good reference implementation
  of coroutine code)
