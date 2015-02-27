from flask import Flask
import requests
from cassandra.cluster import Cluster

app = Flask(__name__)

cluster = Cluster()
session = cluster.connect()


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
