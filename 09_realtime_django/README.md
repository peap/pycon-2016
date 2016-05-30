Reinventing Django for the Real-Time Web
========================================

* https://us.pycon.org/2016/schedule/presentation/1820/
* Channels docs: https://channels.readthedocs.io
* Andrew Godwin

How it's Been
-------------

You take a request, and return a response.

Not only is this how Django views work, but it's true for WSGI, HTTP, Browsers, etc.

Nice and simple. Easy to scale and reason about.

Even HTTP 2 is like this, even though you can send multiple requests and/or
responses at once.

WebSockets
----------

Can send/receive whatever, whenever. What do we do???

How does Django fit in? To answer, think about what Django is:
* easy to use
* secure by default
* hard to break/deadlock
* Python 2 & 3 compatible
* pretty much everything is optional

The solution has to fit those criteria.

Python Concurrency & Django not being async-compatible --> message-passing
* tried and true way of communicating between threads/processes
* similar to request-response, really
* can think of WSGI as the server passing messages to applications, and
  waiting for a response

WebSockets, however, tend to have connections that hang around and are idle
most of the time.

The Channel Layer in Django connects asynchronous socket handling with a
synchronous Django project.

Concepts
--------
*Channels*: named FIFO task queues

*Groups*: named sets of channels you broadcast to

New abstraction: You receive a message, and return zero or more messages.

Receive events from channels, and send events to them/groups.

WebSocket/HTTP messages come with a `reply_channel`.

Installation
------------
`pip install channels` and add to `INSTALLED_APPS`

Liveblog example:
* people open page and get added to named group
* when interesting changes happen, a message is sent to the group

Socket handlers live in `routing.py`

Important Notes
---------------

* Runserver just works with WebSockets now
* Django sessions + auth work with WebSockets
* Generic Consumers exist

Fully worked versions of these examples are at
https://github.com/andrewgodwin/channels-examples

*Channel*: FIFO queue with send and `receive_many` operations, named with a string

*Group*: named set of channels with add/remove/send operations

*Message*: representations for HTTP and WebSocket sessions - defined formats

It's all cross-process

ASGI
----
API spec for channel layer backends

Message formats for HTTP and WebSocket

### Implementation Options for the Channel Layer
Redis: reference network layer

POSIX IPC: for single-machine installs

in-memory: for testing or single-process installs

Other Options
-------------
Because there's a spec, you have options for each layer.

Interface server
* Daphne (HTTP + WS)
* WSGI Adapter (HTTP)

Channel layer:
* asgi\_redis: cross-network, shards
* asgi\_ipc: single-machine

Worker server:
* Django: consumer system
* WSGI Adapter: most WSGI apps

WSGI and/or ASGI
----------------
An ASGI system can serve HTTP and WebSocket... or your WSGI
system can send onto channels

Scaling
-------
* Interface servers scale horizontally.
* Worker servers scale horizontally.
* Channel layer has to, as well.

Being Django
------------
Official external app --> `channels`. 

Will probably be merged in 1.11 or 2.0.

Maturity
--------
Load tests and tweaking in progress.

Still learning from production installs.
