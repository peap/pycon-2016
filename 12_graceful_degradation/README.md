Remote Calls != Local Calls: Graceful Degradation when Services Fail
====================================================================

* https://us.pycon.org/2016/schedule/presentation/2027/
* Dan Riti
* @danriti

Circuit Breaker pattern
-----------------------

`pybreaker`: https://pypi.python.org/pypi/pybreaker

Timeouts + Circuit Breaker pattern

hystrix (netflix, Java) has a nice dashboard for their circuit breakers

Retries
-------
`retry` library for Python

Danger of retries: combinational retry explosion. Example: JS, frontend, and backend
all make four retry attempts, always --> 4^3 == 64 attempts!
