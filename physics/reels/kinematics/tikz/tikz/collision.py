from manim import *
from manim_physics import *

class Collision(SpaceScene):
    def construct(self):
        Circle.set_default(color=WHITE)
        COLLISIONS = [
            ['elastic collision', 1],
            ['inelastic collision', 0.98],
            ['perfectly inelastic collision', 0]
        ]

        OBJECTS = VGroup()

        for col in COLLISIONS:
            S = Line(3.5*LEFT, 3.5*RIGHT)
            C = Circle().next_to(S, 8*UP)
            T = MathTex(f'\\textit{{{col[0]}}}').next_to(S, DOWN).scale(0.5)
            self.add(S, C, T)
            OBJECTS.add(VGroup(S, C, T))

        self.add(OBJECTS.arrange(buff=0.2, direction=DOWN))
        for obj in zip(OBJECTS, COLLISIONS):
            self.make_rigid_body(obj[0][1], elasticity=obj[1][1])
            self.make_static_body(obj[0][0], elasticity=obj[1][1])

        self.wait(30)
