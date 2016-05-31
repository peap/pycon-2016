Better Integration Testing with Cucumber
========================================

* https://us.pycon.org/2016/schedule/presentation/2181/
* Jay Goel (Rent the Runway)

Motivation
----------
Want to make sure new releases actually make a positive impact on users.

Want to accomplish three things with Behavior-Driven Development.
* Increase quality of integration tests
* Reduce regressions
* Focus on _users'_ behavior, rather than _code's_ behavior

So, how does this work?
-----------------------
In any test, we have...
1. preconditions
 * setup work
 * `setUp()`
2. the thing we're testing
 * run the code
 * `test_method()`
3. verification
 * assert things about the results
 * `assert()`

Cucumber is a BDD framework. It has its own DSL. The steps are:
1. Given...
2. When...
3. Then...

Even before writing the actual test code, we have better descriptions of what
the tests are testing. Much better than the long `test_something_is_whatever`
method names in regular tests.

Also, it forces non-technical users (e.g., product managers) to better define
the behavior of software.

BDD is a framework for asking "What are our users actually trying to do?".

Python Libraries
----------------
* Behave (http://pythonhosted.org/behave/)
* Lettuce (http://lettuce.it)

Using Behave for following examples.

Steps in BDD test suites are analogous to routing in HTTP.

Advice
------
Don't be too granular - these tests shouldn't look like code.

Can non-technical people write tests? Not _really_. However, it *is* useful as
a similar language to how we can talk about the software with product managers
and the like.

Jenkins plugin exists! Find it, find it!

Key Takeaways
-------------
* focus on users' needs, not the behavior of code
* "Given... When... Then..." idiom
* our cucumbers can be re-usable and human-understandable
* akin to routes as a separation of concerns
* using language similar to non-technical people is very helpful
