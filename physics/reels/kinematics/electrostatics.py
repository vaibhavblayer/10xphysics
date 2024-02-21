from manim import *
from vmanim import *


class ElectricField(Scene):
    def construct(self):
        equation_one = MathTex(
            r"\boldmath{\vec{E}=-\vec{\nabla} \! \varphi}").scale(1.5).set_color(GRAY_E).move_to(2.5*(RIGHT+UP))

        equation_two = MathTex(
            r"\boldmath{\vec{E}=-\left( \dfrac{\partial \! \varphi}{\partial \! x} \hat{i} + \dfrac{\partial \! \varphi}{\partial \! y} \hat{j} + \dfrac{\partial \! \varphi}{\partial \! z} \hat{k} \right)}").scale(0.75).set_color(RED)
        # self.add(equation_one, equation_two)

        self.play(
            Write(equation_two)
        )
        self.play(
            equation_two.animate.scale(2)
        )
        self.wait(2)

        self.play(
            Unwrite(equation_two)
        )
        self.wait(1)
