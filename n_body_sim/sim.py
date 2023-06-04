import math
from matplotlib import pyplot as plt
from matplotlib import animation
import config
from numba import njit, cuda, jit
from numba.typed import Dict
from numba.types import float64, unicode_type
import numpy as np

data = config.EML4
masses = data['bodies']
frame = data['frame']
PDbodies = [{'mass': mass[0], 'x': mass[1], 'y': mass[2], 'vx': mass[3], 'vy': mass[4], 'name': mass[5], 'colour': mass[6]} for mass in masses]
bodies = []
for mass in masses:
    bodies.append(Dict.empty(key_type=unicode_type, value_type=float64))
    bodies[-1]['mass'] = float(mass[0])
    bodies[-1]['x'] = float(mass[1])
    bodies[-1]['y'] = float(mass[2])
    bodies[-1]['vx'] = float(mass[3])
    bodies[-1]['vy'] = float(mass[4])


nbodies = len(bodies)

timestep = 60 # timestep = 1 day
simtime = 30*24*60*60 # simtime = 1 month
step = 0

body_history = np.array([[np.zeros(1 + simtime//timestep),np.zeros(1 + simtime//timestep)] for _ in bodies])

@jit()
def sim(step, timestep, simtime, bodies, body_history, nbodies):
    while step < simtime:
        for i in range(nbodies):
            body = bodies[i]
            Fg = [0, 0]
            for j in range(nbodies):
                if i != j:
                    other = bodies[j]
                    r = math.sqrt((other['x'] - body['x'])**2 + (other['y'] - body['y'])**2)
                    if r > 0:
                        mFg = ((6.67408*(10**-11))*body['mass']*other['mass'])/(r**2) #6.67408*10**-11
                        theta = math.atan2((other['y'] - body['y']), (other['x'] - body['x']))
                        Fg[0] += mFg*math.cos(theta)
                        Fg[1] += mFg*math.sin(theta)
            body['vx'] += timestep * Fg[0]/body['mass']
            body['vy'] += timestep * Fg[1]/body['mass']

            body_history[i][0][step//timestep] = (bodies[i]['x'])
            body_history[i][1][step//timestep] = (bodies[i]['y'])

        for body in bodies:
            body['x'] += timestep * body['vx']
            body['y'] += timestep * body['vy']
        step += timestep
        print(step/simtime)

sim(step, timestep, simtime, bodies, body_history, nbodies)

bodies = PDbodies

# Create plot with equal scale axes
fig = plt.figure()
ax = fig.add_subplot()

# # Set axes limits
ax.set_xlim(frame[0]-100000, frame[1]+100000)
ax.set_ylim(frame[0]-100000, frame[1]+100000)

# Set axes labels
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_title('N-Body Simulation')

# # plot the results
for i in range(nbodies):
    body = body_history[i]
    ax.plot(body[0], body[1], color=bodies[i]['colour'], label=bodies[i]['name'], linewidth=1)

ax.set_aspect('equal')
#ax.legend()
plt.show()

# # Generate animation

# # Generate high resolution animation
# fig = plt.figure(dpi=300, figsize=(10, 10), facecolor='w', edgecolor='k')
# ax = plt.axes(xlim=(frame[0]-100000, frame[1]+100000), ylim=(frame[0]-100000, frame[1]+100000))
# ax.set_aspect('equal')
# ax.set_xlabel('X (m)')
# ax.set_ylabel('Y (m)')
# ax.set_title('N-Body Simulation')

# lines = []
# for i in range(nbodies):
#     line, = ax.plot([], [], color=bodies[i]['colour'], label=bodies[i]['name'], linewidth=1)
#     lines.append(line)

# def init():
#     for line in lines:
#         line.set_data([], [])
#     return lines

# def animate(i):
#     for j in range(nbodies):
#         body = body_history[j]
#         lines[j].set_data(body[0][max(0, i-1000):i], body[1][max(0, i-1000):i])
#     return lines

# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(body_history[0][0]),interval=1, blit=True).save('n_body_sim.mp4', fps=60, extra_args=['-vcodec', 'h264_nvenc'])

