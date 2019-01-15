from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
_SERVICE_NAME = os.environ.get('REDIS_SERVICE_NAME', 'redis')
_PASSWORD = os.environ.get('REDIS_CONNECTION_PASSWORD', None)
redis = Redis(host=_SERVICE_NAME, port=6379, password=_PASSWORD,
              db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)


@app.route("/hello")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"),
                       hostname=socket.gethostname(), visits=visits)


if __name__ == "__main__":

    # If I enable `debug=True` I get
    # `KeyError: 'getpwuid(): uid not found: 1000060000'` errors
    # from OpenShift.
    app.run(host='0.0.0.0', debug=True)
