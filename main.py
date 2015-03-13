# import requests
import time
import datetime
from datetime import date
from flask import Flask
import flask
# from cassandra.cluster import Cluster

# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py
# (*) Useful Python/Plotly tools
import plotly.tools as tls
# (*) Graph objects to piece together plots
from plotly.graph_objs import *
import plotly.plotly as py
from plotly.graph_objs import *


app = Flask(__name__)


with open('server.conf') as f:
    content = f.readlines()

# cluster = Cluster([content[0].rstrip(),content[1].rstrip(),content[2].rstrip()])
# session = cluster.connect()
# session.set_keyspace('hospital')
s = py.Stream(content[4].rstrip())
s.open()


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/open_stream')
def open_strm():
    s.open()
    return 'Opened Stream!'

@app.route('/close_stream')
def close_strm():
    s.close()
    return 'closed Stream!'

@app.route('/data/<data>')
def data(data):
    date_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # session.execute_async("""
    #     INSERT INTO hospital.data (patient_id, date, event_time, heart_rate)
    #     VALUES (
    #         '1',
    #         %s,
    #         %s,
    #         %s
    #     );
    # """, [date.today().isoformat(), date_time, data])
    array = data.split(",")
    print data
    #STREAM TO GRAPH
    # Current time on x-axis, random numbers HR on y-axis
    x = date_time
    y = int(array[1])

    s.write(dict(x=x, y=y))

    time.sleep(0.08)  # (!) plot a point every 80 ms, for smoother plotting
    return date.today().isoformat() + " " +  date_time + " " + data

# @app.errorhandler(404)
# def page_not_found(e):
#     """Return a custom 404 error."""
#     return 'Sorry, nothing at this URL.', 404
#
# @app.route('/yield/<seconds>')
# def index(seconds):
#     delta = datetime.timedelta(seconds=int(seconds))
#     def inner():
#         now = datetime.datetime.now()
#         before = now - delta
#         now = now.strftime('%Y-%m-%d %H:%M:%S')
#         before = before.strftime('%Y-%m-%d %H:%M:%S')
#
#         results = session.execute_async("""
#     SELECT heart_rate FROM hospital.data
#     WHERE patient_id = '1'
#     AND date = %s
#     AND event_time < %s
#     AND event_time > %s;
# """, [date.today().isoformat(), str(now), str(before)])
#
#         for row in results.result():
#             #time.sleep(1)
#             yield str(row.heart_rate) + '<br/>\n'
#
#     return flask.Response(inner(), mimetype='text/html')
#
# @app.route('/user/<id>')
# def getUser(id):
#
#     results = session.execute_async("""
#     SELECT * FROM hospital.patients
#     WHERE patient_id = %s;
# """, id)
#
#     return "%-30s\t%-20s\t%-20s" % ("name: " + results[0].name + '<br/>\n',
#                                     "email: " + results[0].email + '<br/>\n',
#                                     "address: " + results[0].address)
#
#
# @app.route('/create_user/<id>/<name>/<email>/<address>')
# def create_user(id, name, email, address):
#
#     query = """
#         INSERT INTO hospital.patients (patient_id, name, email, address)
#         VALUES (
#             %s,
#             %s,
#             %s,
#             %s
#         );
#     """
#
#     results = session.execute_async(query, [id, name, email, address])
#
#     return getUser(id)
#
# @app.route('/getHR/<id>/<date>/<start>/<end>')
# def create_user(id, date, start, end):
#
#     query = """
#             SELECT * FROM hospital.data
#             WHERE patient_id = %s
#             AND date= '2015-02-28'
#             AND event_time > %s
#             AND event_time < %s;
#             """
#
#     results = session.execute_async(query, [id, date, start, end])
#
#     return getUser(id)

if __name__ == '__main__':
    app.debug = True
    app.run(host=content[3].rstrip())
