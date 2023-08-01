import numpy as np

def acceleration(body, bodies):
    """Calculate the acceleration on a body due to other bodies."""
    G = 6.67430e-11  # Gravitational constant
    num_bodies = len(bodies)
    acc = np.zeros(2)

    for i in range(num_bodies):
        if bodies[i] is not body:
            r = bodies[i]['position'] - body['position']
            acc += G * bodies[i]['mass'] * r / np.linalg.norm(r)**3

    return acc

def runge_kutta_step(body, bodies, dt):
    """Perform one step of the Runge-Kutta method."""
    k1_v = acceleration(body, bodies) * dt
    k1_p = body['velocity'] * dt

    body['velocity'] += 0.5 * k1_v
    body['position'] += 0.5 * k1_p

    k2_v = acceleration(body, bodies) * dt
    k2_p = (body['velocity'] + 0.5 * k1_v) * dt

    body['velocity'] += 0.5 * k2_v
    body['position'] += 0.5 * k2_p

    k3_v = acceleration(body, bodies) * dt
    k3_p = (body['velocity'] + 0.5 * k2_v) * dt

    body['velocity'] += k3_v
    body['position'] += k3_p

    k4_v = acceleration(body, bodies) * dt
    k4_p = (body['velocity'] + k3_v) * dt

    body['velocity'] += (1/6) * (k1_v + 2*k2_v + 2*k3_v + k4_v)
    body['position'] += (1/6) * (k1_p + 2*k2_p + 2*k3_p + k4_p)

def combine_bodies(body1, body2):
    """Combine two bodies into a single body with conservation of momentum."""
    total_mass = body1['mass'] + body2['mass']
    new_velocity = (body1['mass'] * body1['velocity'] + body2['mass'] * body2['velocity']) / total_mass

    combined_body = {
        'mass': total_mass,
        'position': body1['position'],  # Assuming collision happens at body1's position
        'velocity': new_velocity
    }

    return combined_body

def simulate_n_body_system(bodies, num_steps, dt):
    num_bodies = len(bodies)

    for step in range(num_steps):
        for i in range(num_bodies):
            runge_kutta_step(bodies[i], bodies, dt)

        # Check for collisions and merge bodies
        merged_bodies = []
        for i in range(num_bodies):
            body1 = bodies[i]
            is_collision = False

            for j in range(i+1, num_bodies):
                body2 = bodies[j]
                distance = np.linalg.norm(body1['position'] - body2['position'])

                if distance < 1e-3:  # Assuming collision if the distance is very small (you can adjust this threshold)
                    merged_body = combine_bodies(body1, body2)
                    merged_bodies.append(merged_body)
                    is_collision = True
                    break

            if not is_collision:
                merged_bodies.append(body1)

        bodies = merged_bodies
        num_bodies = len(bodies)

# Create animation of the system

# Bodies is 100 random bodies arranged in a circle
bodies = []
for i in range(50):
    angle = 2*np.pi * np.random.random()
    x = 4e10 * np.cos(angle)
    y = 4e10 * np.sin(angle)
    vx = 4e1 * np.sin(angle)
    vy = -4e1 * np.cos(angle)
    mass = 1e10 * np.random.random() + 1e10
    body = {
        'mass': mass,
        'position': np.array([x, y]),
        'velocity': np.array([vx, vy])
    }
    bodies.append(body)

# add central body with large mass
bodies.append({
    'mass': 1e25,
    'position': np.array([0.0, 0.0]),
    'velocity': np.array([0.0, 0.0])
})

num_steps = 60*60*24*365  # Number of steps to simulate
dt = 2*24*60*60  # Time step (in seconds)

# Create animation using matplotlib, shownig the motion of the bodies
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(-4e11, 4e11), ylim=(-4e11, 4e11))
line, = ax.plot([], [], 'o', markersize=1)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    simulate_n_body_system(bodies, 1, dt)
    x = [body['position'][0] for body in bodies]
    y = [body['position'][1] for body in bodies]
    line.set_data(x, y)
    return line,

# Make animation with high steps per sec

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=num_steps, interval=20, blit=True)
plt.show()

anim.save('n_body_sim1.mp4', fps=60, extra_args=['-vcodec', 'h264_nvenc'])