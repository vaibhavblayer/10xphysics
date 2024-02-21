from vmanim import *
from manim import *

class GenSpiral(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, zoom = self.camera.get_value_trackers()
        t = ValueTracker(0)
        axes = ThreeDAxes().scale(0.5)
        title = RTitle(r"\textit{Helicoid}")

        X = r"x &= \theta\cdot\cos(\phi)\\"
        Y = r"y &= \theta\cdot\sin(\phi)\\"
        Z = r"z &= \phi"
        coords = MathTex(X, Y, Z).shift(5*DOWN)

        def func(u, v):
            return 2*np.array([
                u*np.cos(v), u*np.sin(v), 0.4*v
            ])

        surface = Surface(func)

        surface.add_updater(
            lambda m: m.become(
                Surface(
                    func,
                    u_range=[0, PI],
                    v_range=[0, t.get_value()],
                    resolution=24,
                    checkerboard_colors=[GRAY_C, GRAY_C],
                    stroke_color=GRAY_C,
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
            if t.get_value() <= 4*PI:
                mobject.increment_value(0.5*dt)

        t.add_updater(funct)
        self.play(
            phi.animate.set_value(
                phi.get_value() + 20*DEGREES
            ),
            theta.animate.set_value(
                theta.get_value() + 360*DEGREES
            ),
            zoom.animate.set_value(theta.get_value()*0.4),
            rate_func=rate_functions.linear,
            run_time=30
        )

        self.wait(2)
