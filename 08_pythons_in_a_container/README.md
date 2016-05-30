Pythons in A Container - Lessons Learned Dockerizing Python Micro-Services
==========================================================================

* https://us.pycon.org/2016/schedule/presentation/2096/
* Dorian Pula (SDE @ Points)
* http://dorianpula.ca

Lessons learned the hard way.

What is this talk about?
------------------------
* Lessons learned using Docker for Flask REST APIs and apps.
* Incorporating various tools that Docker and docker-compose provide for better
  DevOps workflow.
* The usefulness of unlearning some accepted patterns in normal Python
  development.

Microservices + Docker
----------------------
Imagine building loyalty program for sprint contributers at PyCon:
* earn points per commit or issue resolved
* redeem for coffee

### Why use microservices?
* divide components that can be worked on concurrently by different teams
* smaller, less complex codebases
* enabled independence between codebases & teams
* more flexible scaling schemes (technologically & organizationally)

Drawbacks:
* distributed codebases are harder to think about, and might contain implicit
  inter-service dependencies
* harder to monitor

### Why Use Docker?
Containers vs. virtual machines
* lighter memory and processing footprint than VMs
* cached, immutable, layered filesystem

Tooling is good (better?)
* quick spin up containers/environments
* easily create, share, and publish images 
* ... (?)

### Docker Compose
Specify all components in one YAML file, then `docker-compose up`.

### Docker Workflow
Docker + Compose replaces a Vagrant + VM workflow:
* `vagrant up` + `vagrant ssh` + run `$app_command` --> `docker run $app_command`
* `vagrant halt` --> `docker stop`
* `vagrant status` --> `docker ps`
* `vagrant provision` --> `docker build`
* `vagrant destroy` --> `docker stop` + `docker rm`
* `vagrant box list`, `remove` --> `docker images`, `rmi`

Lessons
-------

### Make good Docker images

Very important to have good Docker images.

Each step in a Dockerfile can create a new layer in filesystem.
* minimize number of separate `RUN` steps (do `apt-get update` and 
  `apt-get install` in one step, for example)
* make sure layers are cachable
 * cached layer is reused if no checksum change in source --> faster build
* use base images for heavily repeated steps
 * see ONBUILD command for making dynamic base images
* expose ports and volumes to document image

### Python and WSGI apps
Web Servers
* Don't run a web server on your container. Use an external proxy or container
  instead. (e.g., nginx)
* Just run WSGI apps using a WSGI app server like uWSGI or gunicorn

Virtualenv
* don't use it inside containers - not needed
* each container is already an isolated system
* install directly into the container's system site-packages

### Debugging Containers
Want a minimal image, so no SSH daemon... so how do we debug a running container?

Run bash (or other command) on a running service:
`docker-compose exec $SERVICE_NAME /bin/bash`

Inspecting a service's log (STDOUT and STDERR):
`docker-compose logs $SERVICE_NAME`

Inspecting a running container's setup:
* `docker inspect $SERVICE_NAME`
* `docker inspect --format '{{json .Config.Whatever }}' $SERVICE_NAME`

### Persistance, Configs, & Processes
Volume Maps
* changes to container lost after container destroyed.
* Volume maps to external host folder for persistence.
* Another pattern is using separate Docker data containers.

Configuration
* Prefer using environment variables for configuration.
* Volume mapped configs may be a warning sign of an overly complex config
  setup, or config in need of refactoring.

Managing Processes:
* use supervisord or runit to control multiple processes
* consider refactoring containers to not need that

### Testing + Tooling
Testing
* Docker adds consistency in your CI environment
* Simple setup for a Docker host.
* Control over what is in container = repeatable workflow and simpler test environment
* cloud-based CI options with Docker support are out there

Tooling
* docker tool defaults tend to change
* don't build your own tooling if you can avoid it
* if you do need to though, `docker-py` is a python client library for working
with docker

### Deployment and Scaling
Lots of moving parts to consider (load balancers, log aggregation, data
warehousing, etc.)

You're really setting up a private cloud of microservices:
* load balancing + network topology (HAProxy, nginx, etc)
* provisioning
 * automated, repeatable setup for non-Docker systems (Ansible, Puppet & Salt)
* monitoring
 * look at app health, app behavior, and system resources (Nagios, Pingdom, New Relic)
* logging
 * aggregate various logs and correlate events (Splunk)

### Cloud Infrastructure
Managing cloud infr is hard - need tooling and automation, and you don't want to build
your own stuff.

Docker Swarm, Kubernetes, OpenStack Magnum, CoreOS Fleet

## Summary

* Microservices and Docker can improve building and deploying complex systems,
  but neither is a cure-all.
* Good dev and deployment processes matter. Docker has a decent workflow to
  help shape those processes.
* Expect lots of additional infra around microservices
* Avoid building your own tooling
* Use docker containers to do effective isolation
* good app design goes a long way - it enables all this.

## Resources
* Jared Kerim's Django Docker template
 * jaredkerim/django-docker-compose
* 12 Factor apps
 * http://12factor.net
