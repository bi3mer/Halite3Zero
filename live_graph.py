# started from: https://pythonprogramming.net/live-graphs-matplotlib-tutorial/

import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('halite_collected.nsv','r').read().strip()
    lines = [line.split(',') for line in graph_data.split('\n')]
    lines = [[float(split_line[0]), float(split_line[1])] for split_line in lines]

    xs = [i for i in range(len(lines))]
    halite = []
    games_played = []
    for i in range(len(lines)):
    	halite.append(lines[i][0])
    	games_played.append(lines[i][1])

    ax1.clear()
    ax1.plot(xs, halite, label='halite collected')
    ax1.plot(xs, games_played, label='games played')
    ax1.legend(loc='upper center', bbox_to_anchor=(0.5, -0.025), fancybox=True, shadow=True, ncol=2)
    ax1.set_title('Live Training Progress')	

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
