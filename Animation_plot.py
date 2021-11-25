#courtesy: Jie Jenn
#source code : learndataanalysis.org
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(1,1,1)
ax.set_xlim(0,105)
ax.set_ylim(0,12)

x=[]
y=[]
plt.title('Animation graph\n equation: x=10y')
line, = ax.plot(0,0)


def animation_frame(i):
    x.append(i*10)
    y.append(i)
    line.set_xdata(x)
    line.set_ydata(y)

    return line,

animation=FuncAnimation(fig, func=animation_frame, frames=np.arange(0,10,0.01), interval=10)
plt.show()
    
