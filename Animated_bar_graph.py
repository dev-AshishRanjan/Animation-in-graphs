# courtesy: NurelNine (from youtube)
# module: Matplotlib
# animation using pause function. Not by using matplotlib.animation.FuncAnimation

import matplotlib.pyplot as plt
import random

values = [0]*50

for i in range(50):
    values[i] = random.randint(0,100)
    plt.xlim(0,50) #sets the x limit
    plt.ylim(0,100) #sets the y limit
    plt.bar(list(range(50)), values)   #values for bar graph is x:list of 0 to 50 , y:values
    plt.pause(0.0001)   #pauses the interpreter for this much seconds. This is different from time.sleep() function.

plt.show()
