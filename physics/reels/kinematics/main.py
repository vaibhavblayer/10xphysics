from manim import *
from manim_physics import *
# from chanim import *


class Reels(SpaceScene):

    def construct(self):
        ground = Line(LEFT * 2, RIGHT * 2, color=WHITE).shift(2.5*DOWN)
        self.add(ground)
        self.make_static_body(ground)
        forms = [
            r"\textit{average of a function}",
            r"<f(x)>=\dfrac{\int_{x_i}^{x_f} f(x) d\!x}{\int_{x_i}^{x_f} d\!x}"
        ]
        cols = [WHITE, WHITE]
        nums = [1, 2]
        for n, f, col in zip(nums, forms, cols):
            self.GRAVITY = (0, -1)
            text = MathTex(f, color=col).shift(2.5*UP).scale(0.6)
            if n == 1:
                text.scale(0.8)
                self.add(text)
                self.play(Write(text))
                self.wait(3)
            else:
                self.add(text)
                self.play(Write(text))
                self.wait(5)
            self.make_rigid_body(text[0])
            self.wait(5)


class ElectricFieldExample(Scene):
    def construct(self):
        charge1 = Charge(-1, LEFT + DOWN)
        charge2 = Charge(2, RIGHT + DOWN)
        charge3 = Charge(-1, UP)

        def rebuild(field):
            """Funkce která přestaví elektrické pole."""
            field.become(ElectricField(charge1, charge2, charge3))

        field = ElectricField(charge1, charge2, charge3)

        self.add(field, charge1, charge2, charge3)

        self.play(Write(field), FadeIn(charge1),
                  FadeIn(charge2), FadeIn(charge3))

        field.add_updater(rebuild)

        self.play(
            charge1.animate.shift(LEFT),
            charge2.animate.shift(RIGHT),
            charge3.animate.shift(DOWN * 0.5),
            run_time=2,
        )


class MagnetismExample(Scene):
    def construct(self):
        current1 = Current(LEFT * 2)
        current2 = Current(RIGHT * 2, direction=IN)

        def rebuild(field):
            """Funkce která přestaví magnetické pole."""
            field.become(MagneticField(current1, current2))

        field = MagneticField(current1, current2)

        self.play(Write(field), FadeIn(current1), FadeIn(current2))

        field.add_updater(rebuild)

        self.play(
            Rotate(current1, about_point=ORIGIN, angle=4*PI),
            Rotate(current2, about_point=ORIGIN, angle=4*PI),
            run_time=10,
        )


# class ChanimExample(Scene):
#     def construct(self):
#         # internally uses ChemFig syntax (https://www.ctan.org/pkg/chemfig)
#         chem = ChemWithName(
#             "*6((=O)-N(-CH_3)-*5(-N=-N(-CH_3)-=)--(=O)-N(-H_3C)-)",
#             "Caffeine"
#         )

#         chem.move_to(ORIGIN)

#         self.play(chem.creation_anim())
#         self.wait(2)


class ElectricField(Scene):
    def construct(self):
        charge1 = Charge(-1, LEFT + DOWN)
        charge2 = Charge(2, RIGHT + DOWN)
        charge3 = Charge(-1, UP)

        def rebuild(field):
            """Funkce která přestaví elektrické pole."""
            field.become(ElectricField(charge1, charge2, charge3))

        field = ElectricField(charge1, charge2, charge3)

        self.add(field, charge1, charge2, charge3)

        self.play(Write(field), FadeIn(charge1),
                  FadeIn(charge2), FadeIn(charge3))

        field.add_updater(rebuild)

        self.play(
            charge1.animate.shift(LEFT),
            charge2.animate.shift(RIGHT),
            charge3.animate.shift(DOWN * 0.5),
            run_time=2,
        )
