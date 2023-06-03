import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib

def updateline(num, data, line1, data2, line2):
    line1.set_data(data[..., :num])
    line2.set_data(data2[..., :num])
     
    time_text.set_text("Points: %.0f" % int(num))
     
    return line1, line2

class Body():
    def __init__(self, mass, x, y, vx, vy):
        self.mass = mass
        self.velocity = [vx, vy]
        self.x = x
        self.y = y
    def update(self, timestep):
        self.x += self.velocity[0]*timestep
        self.y += self.velocity[1]*timestep

# Array of bodies in format (mass, x, y, vx, vy) for the earth and moon
masses = [[7.3477*10**23, 0, 0, 0, -100],  # earth
          [7.3477*10**22, 384400000, 0, 0, 1022]] # moon

bodies = [Body(mass[0], mass[1], mass[2], mass[3], mass[4]) for mass in masses]
body_history = [[], []]
# simulate for 1 week

timestep = 60 # timestep = 1 minute
step = 0

while step <= 7*24*60*100:
    for body in bodies:
        Fg = [0, 0]
        for other in bodies:
            if other!= body:
                r = math.sqrt((body.x-other.x)**2 + (body.y-other.y)**2)
                if r!= 0:
                    mFg = ((0.000001)*body.mass*other.mass)/(r**2) #6.67408*10**-11
                    theta = math.atan2((+other.y-body.y), (other.x-body.x))
                    Fg = [mFg*math.cos(theta), mFg*math.sin(theta)]

        body.velocity[0] += Fg[0]/body.mass
        body.velocity[1] += Fg[1]/body.mass

    for body in bodies:
        body.update(timestep)
    step += timestep

    for i in range(len(bodies)):
        body_history[i].append([bodies[i].x, bodies[i].y])


# plot the results
# plt.plot([body[0] for body in body_history[0]], [body[1] for body in body_history[0]], label="Earth", color="blue")
# plt.plot([body[0] for body in body_history[1]], [body[1] for body in body_history[1]], label="Moon", color="gray")
# plt.show()

# generating data of 100 elements
# each for line 1
x = [body[0] for body in body_history[0]]
y = [body[1] for body in body_history[0]]
data = np.array([x, y])
 
# generating data of 100 elements
# each for line 2
x2 = [body[0] for body in body_history[1]]
y2 = [body[1] for body in body_history[1]]
data2 = np.array([x2, y2])

# setup the formatting for moving files
Writer = animation.writers['ffmpeg']
Writer = Writer(fps=10, metadata=dict(artist="Me"), bitrate=-1)

fig = plt.figure()
ax = fig.add_subplot(111)
l, = ax.plot([], [], 'b-', label="Earth")
ax2 = ax.twinx()
k = ax2.plot([], [], 'r-', label="Moon")[0]
 
ax.legend([l, k], [l.get_label(), k.get_label()], loc=0)
 
ax.set_xlabel("X")
ax.set_ylabel("Y")

# axis 1
ax.set_ylim(-384400000, 384400000)
ax.set_xlim(-384400000, 384400000)
 
# axis 2
ax2.set_ylim(-384400000, 384400000)
ax2.set_xlim(-384400000, 384400000)

plt.title('Two Body Simulation')
time_text = ax.text(0.1, 0.95, "", transform=ax.transAxes,
                    fontsize=15, color='red')
 
# set line_animation variable to call
# the function recursively
line_animation = animation.FuncAnimation(fig, updateline, frames=7*24*100, fargs=(data, l, data2, k))
line_animation.save("lines.mp4", writer=Writer)
