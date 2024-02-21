from vmanim import *
from manim import *

class GenSphere(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, zoom = self.camera.get_value_trackers()
        t = ValueTracker(0)
        axes = ThreeDAxes().scale(0.5)
        title = RTitle(r"\textit{Sphere}")

        X = r"x &= \cos(\theta)\cdot\sin(\phi)\\"
        Y = r"y &= \sin(\theta)\cdot\sin(\phi)\\"
        Z = r"z &= -\cos(\phi)"
        coords = MathTex(X, Y, Z).shift(5*DOWN)
        
        def func(u, v):
            return 3*np.array([
                np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), -np.cos(v)
            ])

        surface = Surface(
            func,
            u_range=[-PI, PI],
            v_range=[0, 0]
        )

        surface.add_updater(
            lambda m: m.become(
                Surface(
                    func,
                    u_range=[0, 2*t.get_value()],
                    v_range=[0, t.get_value()],
                    resolution=24,
                    checkerboard_colors=[GRAY_C, GRAY_C],
                    stroke_color=GRAY_D,
                )
            )
        )
        self.add_fixed_in_frame_mobjects(title, coords)
        self.set_camera_orientation(
                theta=60 * DEGREES, 
                phi=60 * DEGREES
        )
        self.add(t, axes, surface)

        def funct(mobject, dt):
            if t.get_value() <= PI:
                mobject.increment_value(0.5*dt)

        t.add_updater(funct)
        self.play(
            theta.animate.set_value(
                theta.get_value() + 360*DEGREES
            ),
            rate_func=rate_functions.linear,
            run_time=8
        )
        self.wait(1)
