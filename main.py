import requests
import csv
from flask import Flask
from cassandra.cluster import Cluster


app = Flask(__name__)


with open('server.conf') as f:
    content = f.readlines()



cluster = Cluster([content[0].rstrip(),content[1].rstrip(),content[2].rstrip()])
session = cluster.connect()


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/data/<data>')
def data(data):
    with open('data.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print data
    return data

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


if __name__ == '__main__':
    app.debug = True
    app.run(host=content[3].rstrip())
