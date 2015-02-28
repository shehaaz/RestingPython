import requests
import time
import datetime
from datetime import date
from flask import Flask
import flask
from cassandra.cluster import Cluster




app = Flask(__name__)


with open('server.conf') as f:
    content = f.readlines()

cluster = Cluster([content[0].rstrip(),content[1].rstrip(),content[2].rstrip()])
session = cluster.connect()
session.set_keyspace('hospital')


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/data/<data>')
def data(data):
    session.execute_async("""
        INSERT INTO hospital.data (patient_id, date, event_time, heart_rate)
        VALUES (
            '1',
            %s,
            %s,
            %s
        );
    """, [date.today().isoformat(), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), data])
    print data
    return date.today().isoformat() + " " +  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " " + data

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

@app.route('/yield/<seconds>')
def index(seconds):
    delta = datetime.timedelta(seconds=int(seconds))
    def inner():
        now = datetime.datetime.now()
        before = now - delta
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        before = before.strftime('%Y-%m-%d %H:%M:%S')

        results = session.execute_async("""
    SELECT heart_rate FROM hospital.data
    WHERE patient_id = '1'
    AND date = %s
    AND event_time < %s
    AND event_time > %s;
""", [date.today().isoformat(), str(now), str(before)])

        for row in results.result():
            #time.sleep(1)
            yield str(row.heart_rate) + '<br/>\n'

    return flask.Response(inner(), mimetype='text/html')

@app.route('/user/<id>')
def getUser(id):

    results = session.execute_async("""
    SELECT * FROM hospital.patients
    WHERE patient_id = %s;
""", id)

    return "%-30s\t%-20s\t%-20s" % ("name: " + results[0].name + '<br/>\n',
                                    "email: " + results[0].email + '<br/>\n',
                                    "address: " + results[0].address)


@app.route('/create_user/<id>/<name>/<email>/<address>')
def create_user(id, name, email, address):

    query = """
        INSERT INTO hospital.patients (patient_id, name, email, address)
        VALUES (
            %s,
            %s,
            %s,
            %s
        );
    """

    results = session.execute_async(query, [id, name, email, address])

    return getUser(id)


if __name__ == '__main__':
    app.debug = True
    app.run(host=content[3].rstrip())
