Remote Calls != Local Calls: Graceful Degradation when Services Fail
====================================================================

* https://us.pycon.org/2016/schedule/presentation/2027/
* Dan Riti
* @danriti

Timeouts
--------
Monitor your site to get a feel for what timeout length is appropriate.

Circuit Breaker pattern
-----------------------
Your connection to a service can be in three states:
* closed: connections happening normally
* open: no connections allowed
* half-open: a periodic test request is sent to see if an open circuit should be closed

A Python implementation of the circuit breaker pattern: `pybreaker`
* https://pypi.python.org/pypi/pybreaker
* https://github.com/danielfm/pybreaker

Timeouts + Circuit Breaker pattern - good partners

Hystrix (Netflix, Java) has a nice dashboard for their circuit breakers.

Retries
-------
`retry` library for Python

Danger of retries: combinational retry explosion. Example: JS, frontend, and backend
all make four retry attempts, always --> 4^3 == 64 attempts!
