from manim import *

class RollingWheel(Scene):
    def construct(self):
        # Create a circle to represent the wheel
        wheel = Circle(radius=1, color=BLUE)

        # Create spokes for the wheel
        num_spokes = 8
        spoke_length = 0.8
        spokes = VGroup(*[Line(start=wheel.get_center(), end=wheel.get_center() + spoke_length * rotate_vector(RIGHT, angle), color=WHITE) for angle in np.linspace(0, 2 * PI, num_spokes, endpoint=False)])

        # Create a dot to represent the point of contact with the ground
        contact_point = Dot(radius=0.05, color=RED).move_to(wheel.get_center() - [0, wheel.radius, 0])
        
        # Create an additional red point on the wheel
        additional_point = Dot(radius=0.05, color=RED)
        additional_point.add_updater(lambda m, dt: m.move_to(wheel.get_center() + wheel.radius * rotate_vector(RIGHT, -dt * 2 * PI)))

        # Add the wheel, spokes, contact point, and additional point to the scene
        wheel_and_spokes = VGroup(wheel, spokes)
        animation_group = VGroup(wheel_and_spokes, contact_point, additional_point)
        self.add(animation_group)

        # Animate the wheel's clockwise rolling motion
        self.play(Rotate(animation_group, -2 * PI, about_point=wheel.get_center()), run_time=2)

        self.wait()




# class for simulation of derivative(tangent) of a function



class TangentSim(Scene):
    def construct(self):
        # Create a function graph
        x_range = [-2, 5.5]
        graph = FunctionGraph(lambda x: 0.1 * x ** 3 - 0.5 * x ** 2 + 1, x_range=x_range, color=BLUE)

        # Create a dot on the graph
        dot = Dot(radius=0.05, color=RED).move_to(graph.get_start())

        tracker = ValueTracker(0)
        
        # Create a tangent line to the graph
        tangent_line = TangentLine(graph, alpha=0, length=2, color=RED)

        # add updater to the tangent line
        tangent_line.add_updater(lambda m: m.become(TangentLine(graph, alpha=tracker.get_value(), length=3, color=YELLOW)))
        
        #add updater to the dot
        dot.add_updater(lambda m: m.move_to(graph.point_from_proportion(tracker.get_value())))

        # Add the graph, dot, and tangent line to the scene
        animation_group = VGroup(graph, tangent_line, dot)
        self.add(animation_group)

        # animate the tracker from 0 to 1
        self.play(tracker.animate.set_value(1), run_time=5)


        self.wait()
        
        
        
        
        