#%% Aizawa Attractor :
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


NbPasMax = 1000000

X0 = 0.55
Y0 = -0.51
Z0 = 0.08

def aizawa(x, y, z, a = 0.95, b = 0.7, c = 0.6, d = 3.5, e = 0.25, f = 0.1):
    x_point = (z - b)*x - d*y
    y_point = d*x + (z - b)*y
    z_point = c + a*z - ((z**3)/3) - (x**2) + f * z * (x**3)
    return x_point, y_point, z_point

def aizawa_gen(x0, y0, z0, dt = 0.001):
    x=x0
    y=y0
    z=z0
    while (True) :
        yield x,y,z
        x_point, y_point, z_point = aizawa(x,y,z)
        x += x_point * dt
        y += y_point * dt
        z += z_point * dt

xs=[]
ys=[]
zs=[]

position = iter(aizawa_gen(X0,Y0,Z0))

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
ax.set_title("Aizawa Attractor")
ax.plot(xs, ys, zs, lw=0.5)
plt.show(); 
plt.savefig("Aizawa-Attractor.pdf")
