#%% Equations de Lorentz :
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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
    while (True) :
        yield x,y,z
        x_point, y_point, z_point = lorenz(x,y,z)
        x = x + x_point * dt
        y = y + y_point * dt
        z = z + z_point * dt

xs=[]
ys=[]
zs=[]

position = iter(lorenz_gen(X0,Y0,Z0))

for i in range(0,NbPasMax) :
    x,y,z = next(position)
    xs.append(x)
    ys.append(y)
    zs.append(z)

fig=plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title("Lorentz")
ax.plot(xs, ys, zs, lw=0.5)
plt.show(); 
plt.savefig("Lorentz-Papillon.pdf")