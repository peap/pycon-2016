The cobbler's children have no shoes, or building better tools for ourselves
============================================================================

* https://us.pycon.org/2016/schedule/presentation/2078/
* Alex Gaynor (USDS)

History of tools
----------------

About 5-10 years ago, the only assumption you could make about tool was the
usage of version control.

Issue trackers are now more universal.

Continuous integration are getting more common.

Code review tools are in-vogue.

Deployment automation is very common.

Emerging Trends
---------------

Continous Integration for pull requests, not just trunk and certain branches.

Linting (flake8, pep8, flake8-import-order, bandit, etc.)

Coverage Tracking - automated tracking.

livegrep.com - https://github.com/livegrep/livegrep

mention-bot - suggest reviewers for code reviews, based on people who've
worked on those code lines in the past - github.com/facebook/mention-bot

Workflow - small branch, code, pull request, code review, merge, deploy

Build more tailored tools
-------------------------

Automation > Process
* tools are better than manual processes
* tools are encoded processes - more visibility
* you always know what the correct behavior is

Lots of existing tools have APIs we can leverage. (GitHub, for example)

GitHub issues APIs:
* create an issue
* add/remove labels
* add a comment
* assign to someone

GitHub PRs:
* send a PR
* assign a PR
* add/remove labels
* leave a code review
* statuses

github3.py - create single-use accounts for authenication

Example Tools
-------------

HTTPS certificate expiration:
* scan hosts, check `notAfter`, file issue if time < cut-off
* could have it leave comments as the days tick by

Auto-labeling of pull requests:
* watch for a certain file in a pull request and attach label

requirements.txt bumper:
* update all our repos when a new Django security release is issued

UI change reviewer:
* it's hard to review changes to a UI
 * can be hard to tell if something *has* changed
 * if you *do* notice, it can be hard to tell if it's "correct"
* Write a service that GitHub/Travis calls with a screenshot that leaves a
  comment on the pull request if there's a change. Just tells a human reviewer
  *that* the screenshot changed, and let them decide if it's ok.

Approval process commit status:
* watch for comments from certain people to enable mergability for a PR
