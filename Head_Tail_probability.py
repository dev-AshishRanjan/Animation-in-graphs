# courtesy: NurelNine (from youtube)
# module: Matplotlib

import matplotlib.pyplot as plt
import random

heads_tails = [0,0]

for i in range(10000):
    if i%50 == 0:    #if i is divisible by 50
        heads_tails[random.randint(0,1)] +=1
        plt.bar([0,1], heads_tails,  color=('blue', 'red'))    #values for bar graph is x:0 and 1 , y:heads_tails
        plt.pause(0.001)    #pauses the interpreter for this much seconds. This is different from time.sleep() function.

#plt.legend()   #kind  of not needed here
plt.show()
