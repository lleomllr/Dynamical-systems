#%%Ikeda Map
import numpy as np
import plotly.graph_objects as go
import math 
import matplotlib.pyplot as plt 

def t_n(x, y):
  return 0.4 - (6 / (1 + x**2 + y**2))

def ikeda(u, x, y):
  t = t_n(x, y)
  x_n = 1 + u * (x * math.cos(t) - y * math.sin(t))
  y_n = 1 + u * (x * math.sin(t) + y * math.cos(t))
  return x_n, y_n

def ikeda_gen(u, x0, y0, n=10000):
  x = np.zeros(n)
  y = np.zeros(n)
  x[0] = x0
  y[0] = y0
  
  for i in range(1, n):
    x[i], y[i] = ikeda(u, x[i-1], y[i-1])
  
  return x, y

u = 0.992
x0, y0 = 0.01, 0.01
n = 20000

x, y = ikeda_gen(u, x0, y0, n)

fig = go.Figure()
fig.add_trace( 
    go.Scatter(
        x=x, 
        y=y, 
        mode='lines',
        marker=dict(
            size=2,
            color=np.arange(n),  
            colorscale='Viridis',
            showscale=True
        ),
        name='Ikeda Map'
    )
)
fig.update_layout( 
    scene = dict(
       xaxis_title='x',
       yaxis_title='y', 
    ),
    title='Ikeda Map', 
    width = 800, 
    height = 700
)
fig.show()
