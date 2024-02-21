from manim import *


class Geometry(ThreeDScene):
    def construct(self):

        circle = Cone()

        self.add(circle)
        self.play(
            Create(circle)


        )


class MagneticFieldScene(ThreeDScene):
    def construct(self):
        # Create a 3D coordinate system
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        # Add the 3D coordinate system to the scene
        self.add(axes)

        # Initialize particle parameters
        charge = 1  # Particle charge
        mass = 1    # Particle mass
        # Initial velocity of the particle
        velocity = np.array([1.0, 0.0, 0.0])
        magnetic_field = np.array([0, 0, 1])  # Uniform magnetic field

        # Simulate particle's trajectory
        particle = Sphere(color=YELLOW, radius=0.1)
        particle.move_to(ORIGIN)
        self.add(particle)

        time_step = 0.01  # Time step for simulation
        num_steps = 100  # Number of simulation steps

        for _ in range(num_steps):
            # Lorentz force equation
            lorentz_force = charge * np.cross(velocity, magnetic_field)
            acceleration = lorentz_force / mass
            velocity += acceleration * time_step
            particle.shift(velocity * time_step)

            self.wait(time_step)


tree = []


def branch(root, n):
    # root_left = root + [np.cos(PI-PI/6), np.sin(PI-PI/6), 0]
    root_right = root + [np.cos(PI/6), np.sin(PI/6), 0]
    if n == 1:
        tree.append(
            Line(root, root_right)
        )
        # tree.append(
        #     Line(root, root_left)
        # )
    else:
        print(root_right)
        branch(root_right, n-1)
        # branch(root_left, n-1)


class Tree(Scene):
    def construct(self):
        begin = 2*DOWN
        end = UP
        branch(begin, 4)
        for i in tree:
            self.add(i)
