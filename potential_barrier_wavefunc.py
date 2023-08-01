import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import find_peaks

# Constants
hbar = 1.0  # Reduced Planck's constant (set to 1 for simplicity)
mass = 1.0  # Particle mass (set to 1 for simplicity)

# Simulation parameters
L = 50.0  # Length of the region
Nx = 10000  # Number of spatial grid points
Nt = 300  # Number of time steps
dt = 0.01  # Time step

# Spatial grid
x = np.linspace(-L/2, L/2, Nx)
dx = x[1] - x[0]

# Initial wavefunction parameters
sigma = 0.5  # Width of the initial wavefunction
k0 = 20.0  # Wavevector of the initial wavefunction

# Initial wavefunction psi(x)
psi0 = np.exp(-(x**2) / (2 * sigma**2)) * np.exp(1j * k0 * x)

# Potential barrier parameters
barrier_start = 2.0  # Start position of the barrier
barrier_width = 0.5  # Width of the barrier
barrier_height = 5.0  # Height of the barrier

# Potential barrier function V(x)
V = np.zeros_like(x)
V[(x >= barrier_start) & (x <= barrier_start + barrier_width)] = barrier_height

# Animation setup
fig, ax = plt.subplots()
line_real, = ax.plot(x, np.real(psi0), 'b', label='Real part')
line_imag, = ax.plot(x, np.imag(psi0), 'g', label='Imaginary part')
line_prob, = ax.plot(x, np.abs(psi0)**2, 'r', label='Probability density')
line_barrier = ax.fill_between(x, 0, V, color='gray', alpha=0.2, label='Potential Barrier')

ax.set_xlim(-5+barrier_start, 5+barrier_start)
#ax.set_ylim(-1, np.max(np.abs(psi0)**2 + barrier_height) * 1.2)
ax.set_ylim(-2, 5)
# ax.set_xlabel('Position (x)')
# ax.set_ylabel('Wavefunction')
# ax.set_title(f"wavevector = {k0}, sigma = {sigma}, barrier height = {barrier_height}")
ax.legend()

# Function to label the peaks in the probability density plot
def label_peaks():
    peaks, _ = find_peaks(np.abs(psi0)**2, height=barrier_height)
    for peak_x in x[peaks]:
        ax.text(peak_x, np.abs(psi0[peaks][np.abs(x[peaks]-peak_x).argmin()])**2, f'Peak at x={peak_x:.2f}', rotation=90, ha='center', va='bottom', fontsize=8)

def init():
    line_real.set_ydata(np.real(psi0))
    line_imag.set_ydata(np.imag(psi0))
    line_prob.set_ydata(np.abs(psi0)**2)
    return line_real, line_imag, line_prob, line_barrier

def animate(i):
    global psi0
    # Split-step Fourier method
    psi_half = np.fft.fft(psi0) * np.exp(-1j * dt * (hbar / (2 * mass)) * np.fft.fftfreq(Nx, dx)**2)
    psi0 = np.fft.ifft(psi_half) * np.exp(-1j * dt * V / hbar)
    
    # Update the plot data
    line_real.set_ydata(np.real(psi0))
    line_imag.set_ydata(np.imag(psi0))
    line_prob.set_ydata(np.abs(psi0)**2)

    # Clear previous peak labels
    ax.texts.clear()

    # Label the peaks in the probability density plot for the current frame
    label_peaks()
    
    return line_real, line_imag, line_prob, line_barrier

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=Nt*5, interval=1, blit=True)
ani.save('potential_barrier_wavefunc.mp4', fps=60, extra_args=['-vcodec', 'h264_nvenc'])
plt.show()
