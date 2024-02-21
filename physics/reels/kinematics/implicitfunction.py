
from manim import *

from functions import *

from sympy import singularities, Symbol
x = Symbol('x', real=True)


class Main(Scene):
    config.frame_width = 13.5
    config.frame_height = 24.0
    config.pixel_width = 1350
    config.pixel_height = 2400
    config.frame_rate = 60
    config.transparent = True

    def construct(self):
        Tex.set_default(color="#28282B")
        Line.set_default(color="#28282B")
        Mobject.set_default(color="#28282B")
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=13,
            y_length=13,
            tips=False,
        )
        myTemplate = TexTemplate(preamble=r"\usepackage[utopia]{mathdesign}")
        title = Tex(fx_l_list[0], tex_template=myTemplate).shift(7.5*UP)

        eq = Tex(fx_l_list[1], tex_template=myTemplate)

        self.add(title, ax)

        graph_i = ax.plot(
            lambdify(x, fx_list[0]),
            discontinuities=list(singularities(fx_list[0], x))
        )
        equation_i = Tex(fx_l_list[0], tex_template=myTemplate).shift(7.5*DOWN)
        for i, j in zip(fx_list, fx_l_list):
            graph = ax.plot(
                lambdify(x, i),
                discontinuities=list(singularities(i, x))
            )
            graph_n = ax.plot(
                lambdify(x, -i),
                discontinuities=list(singularities(i, x))
            )
            equation = Tex(j, tex_template=myTemplate).shift(7.5*DOWN)
            if fx_list.index(i) == 0:
                self.play(
                    Create(graph_i),
                    Write(equation_i)
                )
                self.wait()

            elif fx_list.index(i) == (len(fx_list) - 1):

                self.play(
                    Transform(graph_i, graph),
                    Transform(graph_n, graph_n),
                    Transform(equation_i, equation)
                )
                self.wait(2)
                self.play(
                    Circle(
                        radius=0.1, color=BLACK, fill_opacity=1).animate.scale(200)
                )

            else:
                self.play(
                    Transform(graph_i, graph),
                    Transform(equation_i, equation)
                )
                self.wait()
