# PySimple
A very simple Python application. Using the material in Docker's
[Get Started] guide this is a simple (classic) Python-based web-app
that uses Flask and Redis. You don't have to understand any of this,
the goal of this project is simply to provide a stable base for
demonstrating Docker.

You should be able to build and run the containerised app using
any suitably equipped Docker host. I used a `Mac` and Docker
community edition `v17.06.2`.

## Building
Build and tag the image...

    $ docker build -t friendlyhello .

And run it (in detached/non-blocking mode)...

    $ docker run -d -p 4000:8080 friendlyhello
    <container ID>

This will start the image as a container and map host port `4000` into the
container, appearing on port `8080` internally. This port re-mapping
is an essential part of the Docker ecosystem. The _long-and-short_ of all
of this is that you should now be able to connect to the app at
`http://localhost:4000`:

    $ curl http://localhost:4000
    
Now stop your container and remove the stopped container using its ID:

    $ docker stop <container ID>
    $ docker rm <container ID>

## Deploying
Here, we'll deploy to the Docker hub. It's free and simple. We just need to
tag our image (with something useful like `2017.1`) and then push it.

    $ docker login -u alanbchristie
    [...]
    $ docker tag friendlyhello alanbchristie/pysimple:2017.1
    $ docker push alanbchristie/pysimple:2017.1

>   Here my hub account is `alanbchristie` and the repository setup there
    is `pysimple`. We're giving this image the tag `2017.1`.
    
>   Tags are handled very differently in Docker, it does not understand
    that `1` is better than `2` - they're just strings that happen to
    also be numbers.

With the Docker image pushed we can now run the application on any
Docker-enabled machine with the command:

    $ docker run -d -p 4000:8080 alanbchristie/pysimple:2017.1
    Unable to find image 'alanbchristie/pysimple:2017.1' locally
    2017.1: Pulling from alanbchristie/pysimple
    [...]

## Deploying to OpenShift
The `openshift/templates` directory contains a `pysimple.yml` file
that acts as a template for the application. You can install this
in your OpenShift cluster to allow deployment using the *Catalogue*.

If you've logged into your cluster you should be able to
load the template definition into the `openshift` project like this: -

    $ cd openshift/templates
    $ oc create -f pysimple.yml -n openshift

>   The template defines a **DeploymentConfig** for the Pod (Container),
    a **Service** and a **Route**.

With the template installed you should be able to select it using
**Add to Project** where you'll find PySimple as an application.

You will need toi install Redis into your chosen project
(Redis should already be an available template application)
before installing a **PySimple** instance.

---

_Alan B. Christie_  
_January 2018_  

[Get Started]: https://docs.docker.com/get-started/part2/
