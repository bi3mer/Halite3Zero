# https://pythonprogramming.net/live-graphs-matplotlib-tutorial/

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('halite_collected.nsv','r').read()
    lines = graph_data.split('\n')
    xs = [i for i in range(len(lines) - 1)]
    ys = []
    for line in lines:
        if len(line) > 1:
            ys.append(float(line))

    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
