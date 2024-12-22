import numpy as np
import plotly.graph_objects as go

NbPasMax = 10000

X0 = 0.
Y0 = 2.
Z0 = 10.

def lorenz(x, y, z, s=10, p=28, b=8/3):
    x_point = s*(y - x)
    y_point = p*x - y - x*z
    z_point = x*y - b*z
    return x_point, y_point, z_point

def lorenz_gen(x0, y0, z0):
    x=x0
    y=y0
    z=z0
    dt = 0.01
    while True:
        yield x, y, z
        x_point, y_point, z_point = lorenz(x, y, z)
        x = x + x_point * dt
        y = y + y_point * dt
        z = z + z_point * dt

xs = []
ys = []
zs = []

position = iter(lorenz_gen(X0, Y0, Z0))

for i in range(0, NbPasMax):
    x, y, z = next(position)
    xs.append(x)
    ys.append(y)
    zs.append(z)

fig = go.Figure(data=[go.Scatter3d(x=xs, y=ys, z=zs, mode='lines', line=dict(width=1))])

fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
    title='Lorenz Butterfly'
)
fig.show()
