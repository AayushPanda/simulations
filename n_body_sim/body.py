class Body():
    def __init__(self, mass, x, y, vx, vy, name, colour):
        self.mass = mass
        self.velocity = [vx, vy]
        self.position = [x, y]
        self.name = name
        self.colour = colour
    def update(self, timestep):
        self.position[0] += self.velocity[0]*timestep
        self.position[1] += self.velocity[1]*timestep