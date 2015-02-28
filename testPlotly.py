import datetime
import time
# (*) To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py

# (*) Useful Python/Plotly tools
import plotly.tools as tls

# (*) Graph objects to piece together plots
from plotly.graph_objs import *

import numpy as np  # (*) numpy for math functions and arrays
import plotly.plotly as py
from plotly.graph_objs import *


with open('server.conf') as f:
    content = f.readlines()

#auto sign-in with credentials or use py.sign_in()
stream = Stream(
    token=content[4].rstrip(),  # (!) link stream id to 'token' key
    maxpoints=36000      # (!) keep a max of 80 pts on screen
)

heart_rate = Scatter(
        x=[],
        y=[],
        stream=stream
    )
data = Data([heart_rate])

# Add title to layout object
layout = Layout(title='Time Series')

# Make a figure object
fig = Figure(data=data, layout=layout)

# (@) Send fig to Plotly, initialize streaming plot, open new tab
unique_url = py.plot(fig, filename='Heart Rate Monitor')
#
# s = py.Stream(content[4].rstrip())
#
# s.open()
#
# i = 0    # a counter
# k = 5    # some shape parameter
# N = 200  # number of points to be plotted
#
# # Delay start of stream by 5 sec (time to switch tabs)
# time.sleep(5)
#
# while i<N:
#     i += 1   # add to counter
#
#     # Current time on x-axis, random numbers on y-axis
#     x = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#     y = (np.cos(k*i/50.)*np.cos(i/50.)+np.random.randn(1))[0]
#
#     # (-) Both x and y are numbers (i.e. not lists nor arrays)
#
#     # (@) write to Plotly stream!
#     s.write(dict(x=x, y=y))
#
#     # (!) Write numbers to stream to append current data on plot,
#     #     write lists to overwrite existing data on plot (more in 7.2).
#
#     time.sleep(0.08)  # (!) plot a point every 80 ms, for smoother plotting
#
# # (@) Close the stream when done plotting
# s.close()
