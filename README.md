# PySimple

![GitHub](https://img.shields.io/github/license/alanbchristie/pysimple)
[![Build Status](https://travis-ci.org/alanbchristie/PySimple.svg?branch=master)](https://travis-ci.org/alanbchristie/PySimple)
![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/alanbchristie/pysimple)

![Ansible Role](https://img.shields.io/ansible/role/42199)

A very simple [Python] application. Using the material in Docker's
[Get Started] guide this is a simple (classic) Python-based web-app
that uses Flask and Redis. You don't have to understand any of this,
the goal of this project is simply to provide a stable base for
demonstrating Docker.

You should be able to build and run the containerised app using
any suitably equipped Docker host. I used a `Mac` and Docker
community edition `v19.03.2`.

## Building
Build and tag the image...

    $ docker build -t friendlyhello .

And run it (in detached/non-blocking mode)...

    $ docker run -d -p 4000:8080 friendlyhello
    <container ID>

This will start the image as a container and map host port `4000` into the
container's on port `8080`. This port re-mapping is an essential part of the
Docker ecosystem. The _long-and-short_ of all of this is that you should now
be able to connect to the app at `http://localhost:4000`:

    $ curl http://localhost:4000
    
Now stop your container and remove the stopped container using its ID:

    $ docker stop <container ID>
    $ docker rm <container ID>

You can also use `docker-compose` and the built-in `docker-compose.yml`
configuration file to spin-up more than one container. In our compose
file also start a [Redis] container, a simple database that the app will
use (if it can) to count the number of visits made to its port.

    $ docker-compose build
    $ docker-compose up --detach

>   The docker-compose configuration exposes the application container
    using port 8080 on the local host.

And stop and remove the containers with: -

    $ docker-compose down
     
## Deploying to Docker Hub
Here, we'll deploy to the Docker hub. It's free and simple. We just need to
tag our image (with something useful like `2019.3`) and then push it.

    $ docker login -u alanbchristie
    [...]
    $ docker build -t alanbchristie/pysimple:2019.6 .
    $ docker push alanbchristie/pysimple:2019.6

>   Here my hub account is `alanbchristie` and the registry there
    is `pysimple`. We're giving this image the tag `2019.6`.
    
>   Tags are handled very differently in Docker, it does not understand
    that `1` is better than `2` - they're just strings that happen to
    also be numbers.

With the Docker image pushed we can now _pull_ the application onto any
Docker-enabled machine and run it with the command:

    $ docker run -d -p 4000:8080 alanbchristie/pysimple:2019.6
    Unable to find image 'alanbchristie/pysimple:2017.6' locally
    2019.3: Pulling from alanbchristie/pysimple
    [...]

## Building for ARM (k3s)
To build and push an image for the ARM processor (suitable for a Raspberry-Pi
Kubernetes/k3s deployment): -

    $ docker build --build-arg from_image=arm32v7/python:3.7.4-alpine3.10 \
        -t alanbchristie/pysimple:arm32v7-latest .
    $ docker push alanbchristie/pysimple:arm32v7-latest

## Related repositories
The following related GitHub repositories might be of interest: -

-   The PySimple Ansible Galaxy [Role]
-   The PySimple Ansible [Operator]

---

_Alan B. Christie_  
_November 2019_  

[Get Started]: https://docs.docker.com/get-started/part2/
[Operator]: https://github.com/alanbchristie/ansible-operator-PySimple
[Python]: https://www.python.org
[Redis]: https://redis.io
[Role]: https://github.com/alanbchristie/ansible-role-PySimple
