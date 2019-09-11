from flask import Flask
from redis import Redis, RedisError
import os
import socket
import pickledb

# Connect to Redis
redis = Redis(host="redis", port=6379,
              db=0, socket_connect_timeout=2, socket_timeout=2)
# ...or a local (file-based) Pickle DB
pickle_db = pickledb.load('/data/pysimple.db', True)

COUNTER_FIELD = 'counter'

app = Flask(__name__)


@app.route("/")
def hello():
    try:
        visits = redis.incr(COUNTER_FIELD)
    except RedisError:
        visits = pickle_db.get(COUNTER_FIELD)
        if not visits:
            visits = 0
        visits += 1
        pickle_db.set(COUNTER_FIELD, visits)

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Num visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"),
                       hostname=socket.gethostname(), visits=visits)


if __name__ == "__main__":

    # If I enable `debug=True` I get
    # `KeyError: 'getpwuid(): uid not found: 1000060000'` errors
    # from OpenShift.
    app.run(host='0.0.0.0', port=8080)
