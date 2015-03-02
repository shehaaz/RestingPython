import time
import datetime
from datetime import date
# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py
# (*) Useful Python/Plotly tools
import plotly.tools as tls
# (*) Graph objects to piece together plots
from plotly.graph_objs import *
import plotly.plotly as py
from plotly.graph_objs import *
import random

with open('server.conf') as f:
    tokens = f.readlines()

s = py.Stream(tokens[4].rstrip())
s.open()


while 1:
    time.sleep(1)
    #STREAM TO GRAPH
    # Current time on x-axis, random numbers on y-axis
    x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    y = random.randint(60, 80)
    print str(x) + "," + str(y)
    s.write(dict(x=x, y=y))

s.close()
