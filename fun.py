import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

rolls =[]

fig, ax = plt.subplots()
ax.set_title("Rolling a Die")

def roll_die(frames):
    ax.clear()
    rolls.append(np.random.randint(1,7))

    counts=[rolls.count(i) for i in range(1,7)]

    ax.bar(range(1,7), counts)
    ax.set_xticks(range(1,7))

    ax.set_ylim(0, max(counts)+1)


ani = FuncAnimation(fig, roll_die, frames=100, repeat=False)
plt.show()
