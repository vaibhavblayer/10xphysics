from manim import *
from manim_physics import *


class ConvexLens(Scene):
    def construct(self):
        lens_style = {"fill_opacity": 0.5, "color": BLUE}
        L1 = Lens(5, 1, **lens_style).shift(LEFT)

        b = [
            Ray(LEFT * 5 + UP * i, RIGHT, 8, [L1], color=RED)
            for i in np.linspace(-2, 2, 10)
        ]
        self.add(L1, *b)


class ConvexLensShortApperture(Scene):
    def construct(self):
        lens_style = {"fill_opacity": 0.5, "color": BLUE}
        L1 = Lens(5, 1, **lens_style).shift(LEFT)

        b = [
            Ray(LEFT * 5 + UP * i, RIGHT, 8, [L1], color=RED)
            for i in np.linspace(-1, 1, 10)
        ]
        self.add(L1, *b)


class ConcaveLensShortApperture(Scene):
    def construct(self):
        lens_style = {"fill_opacity": 0.5, "color": BLUE}
        L1 = Lens(-5, 0.5, **lens_style).shift(LEFT)

        b = [
            Ray(LEFT * 5 + UP * i, RIGHT, 8, [L1], color=RED)
            for i in np.linspace(-1, 1, 10)
        ]
        self.add(L1, *b)


class ConvexPlusConcave(Scene):
    def construct(self):
        lens_style = {"fill_opacity": 0.5, "color": BLUE}
        L1 = Lens(5, 1, **lens_style).shift(LEFT)
        L2 = Lens(-5, 0.5, **lens_style).shift(RIGHT)

        b = [
            Ray(LEFT * 5 + UP * i, RIGHT, 8, [L1], color=RED)
            for i in np.linspace(-1, 1, 10)
        ]

        self.add(L1, L2, RAYS)
        RAYS.add_updater(update_b)
        self.wait(2)
