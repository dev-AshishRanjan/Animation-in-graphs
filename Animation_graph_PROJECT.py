import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
x=[]
y=[]
ax.set_xlim(0,10)
ax.set_ylim(-50,1000)

line,=ax.plot(0,0)


def f(i):
    x.append(i)
    y.append(i**3)
    line.set_xdata(x)
    line.set_ydata(y)

    return line,

animation=FuncAnimation(fig, f, frames=np.random.rand(100)*10, interval=100)
plt.show()
#we are having a problem:
#a line is unexpectedly drawn joining origin to finish point
