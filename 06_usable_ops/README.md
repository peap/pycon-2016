Usable Ops: How to make web infrastructure management easier.
=============================================================

* https://us.pycon.org/2016/schedule/presentation/2135/
* Kate Heddleston, Joyce Jang
* kateheddleston.com, joycejang.com

Why This Talk?
--------------
Talk comes from experience in engineering on-boarding processes.

Deployment process is a big pain point, and most of the problems companies
have with deployments are human problems.

Usable Obs
----------

* What is usability?
* Why is it important for web infrastructure?
* How do we build usable web infrastructure?

### What is usability?
- See: The Design of Everyday Things

* How do you turn on a light? Not always easy (for example, in conference hall),
and still lots of choices for homes.
* How do you set your shower temperature?
* How do you open a door?

*Affordances* - the ways an object tells you how to interact with it. For a
teapot, the handle affords handling: pick me up here. Also about
discoverability.

What are the consequences of bad usability? Ranges from minor annoyances, to
embarassment, to death.

Botts dots: raised, reflective dots added to lane markers in the 1950s. Improved
the usability of roads.

Web infrastructure should be usable, understanable, safe to use.

### Why is it important for web infrastructure?
Web infrastructure *is* a man-made object, even though it's fairly abstract.

Consequences for bad usability for web infrastructure:
* errors
* scalability
* friction

If tests are too complicated, new hires *and* the existing team will avoid
them, or use them incorrectly.

Human-usable access points are important. Design these well and don't make them
dangerous.

    If your system is too complex for your entire team to use safely, it is too
    complex. Period.

Friction between teams can create demotivation and attrition. (Application
engineers vs. devops engineers, for example.)

Usability vs. Security - they are separate concerns. Security through
complexity isn't useful. Good usability doesn't cost you security. Added
complexity doesn't increase security.

### How do we build usable web infrastructure?

How do you navigate your web system? Three questions:
* How do you change system installations?
 * Recommendation: use containers, rather than separate Chef/Ansible/Puppet
   scripts.
 * Containers are more usable: Dockerfile lives next to the code. Changes
   are enacted on the next build. One workflow > two workflows.
 * Containers also *link* these system installations to code changes.
* How do you deploy your code?
 * one-click deploys are great
 * automate away as much of the technical process as possible
 * build good abstractions, in general
* How do you know where you are in the system?
 * build navigation and collaboration tools
 * dedicated web app to show the infrastructure and how its all connected
 * no wiki pages! real-time, interactive diagrams

Automate core processes. Expose human interaction points.

When in doubt, consult Nielsen's 10 Usability Heuristics:
https://www.nngroup.com/articles/ten-usability-heuristics/
