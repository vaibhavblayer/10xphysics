from threading import Thread
from manim import *
from vmanim import *


class Modulus(Scene):
    # config.frame_rate = 10

    def construct(self):
        Tex.move_to(
            [-3.2, 1.2, 0]
        ).scale(0.75)
        ax = Axes(
            x_range=[-5, 6, 1],
            y_range=[-5, 6, 1],
            x_length=8,
            y_length=8,
            tips=False,
        ).shift(DOWN)

        function = "$f(x)=||x|^2-2|x|-3|$"
        title = Title(function, include_underline=False)

        eq = Tex(r"$x^2-2x-3$")
        eq1 = Tex(r"$|x|^2-2|x|-3$")
        eq2 = Tex(r"$||x|^2-2|x|-3|$")

        graph = ax.plot(
            lambda x: x**2-2*x-3,
            x_range=(-4, 4, 0.001),
        ).set_color(BLUE_D)

        graph1 = ax.plot(
            lambda x: abs(x)**2-2*abs(x)-3,
            x_range=(-4, 4, 0.001),
        )

        graph2 = ax.plot(
            lambda x: abs(abs(x)**2-2*abs(x)-3),
            x_range=(-4, 4, 0.001),
        )

        self.add(title, ax)
        self.wait(1/30)
        self.play(
            Create(graph),
            Write(eq),
            Flash(eq, color=WHITE, flash_radius=0.5)
        )
        self.wait()
        self.play(
            Transform(graph, graph1),
            Transform(eq, eq1)
        )
        self.wait()
        self.play(
            Transform(graph, graph2),
            Transform(eq1, eq2)
        )
        self.wait(3)


class Tranformation(Scene):

    def construct(self):

        ax = Axes(
            x_range=[-5, 6, 1],
            y_range=[-5, 6, 1],
            x_length=8,
            y_length=8,
            tips=False,
        ).shift(DOWN)

        function = "$f(x)=||x|^2-2|x|-3|$"
        title = Title(function, include_underline=False)

        eq = Tex(r"$x^2-2x-3$").move_to([-3.2, 1.2, 0]).scale(0.75)
        eq1 = Tex(r"$|x|^2-2|x|-3$").move_to([-3.2, 1.2, 0]).scale(0.75)
        eq2 = Tex(r"$||x|^2-2|x|-3|$").move_to([-3.2, 1.2, 0]).scale(0.75)

        graph = ax.plot(
            lambda x: x**2-2*x-3,
            x_range=(-4, 4, 0.001),
        ).set_color(BLUE_D)

        def f1(x): return x**2-2*x-3
        def f2(x): return abs(x)**2-2*abs(x)-3
        def f3(x): return abs(abs(x)**2-2*abs(x)-3)

        graph_left = ax.plot(f1, x_range=(-4, 0, 0.001))
        graph_right = ax.plot(f1, x_range=(0, 4, 0.001))
        graph_left_m = ax.plot(f2, x_range=(-4, 0, 0.001))
        graph_right_m = ax.plot(f2, x_range=(0, 4, 0.001))
        graph_left_M = ax.plot(f3, x_range=(-4, 0, 0.001))
        graph_right_M = ax.plot(f3, x_range=(0, 4, 0.001))

        graph2 = ax.plot(
            lambda x: abs(abs(x)**2-2*abs(x)-3),
            x_range=(-4, 4, 0.001),
        )

        self.add(title, ax)
        self.wait(1/30)
        self.play(
            Create(graph_left),
            Create(graph_right),
            Write(eq),
            Flash(eq, color=WHITE, flash_radius=0.5)
        )
        self.wait()
        self.play(FadeOut(graph_left, shift=DOWN))
        self.play(FadeIn(graph_left_m, shift=LEFT), Transform(eq, eq1))
        self.play(
            Transform(graph_left_m, graph_left_M),
            Transform(graph_right, graph_right_M),
            Transform(eq1, eq2)
        )
        self.wait()


class CubicGraph(Scene):
    def construct(self):
        ax = RAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
        )
        x3 = ax.plot(
            lambda x: x**3,
            x_range=(-1.25, 1.25, 0.001)
        )

        def fx13(x):
            if x >= 0:
                return x**(1/3)
            else:
                return -(-x)**(1/3)

        x13 = ax.plot(
            fx13,
            x_range=(-1.5, 1.5, 0.001)
        )

        x = ax.plot(
            lambda x: x,
            x_range=(-1.5, 1.5, 0.001),
            color=GRAY_B,
            stroke_width=1
        )

        x3_l = ax.get_graph_label(
            x3, "x^3", x_val=1.25, direction=UP
        )

        x13_l = ax.get_graph_label(
            x3, "x^{1/3}", x_val=1.5, direction=21*DOWN
        )

        self.add(ax)
        self.play(
            Succession(
                Create(x3),
                Write(x3_l)
            ),

            run_time=3
        )

        self.play(
            Create(x)
        )
        self.play(
            Succession(
                Create(x13),
                Write(x13_l)
            ),
            run_time=3
        )

        self.wait(3)


class CosInverse(Scene):
    def construct(self):
        ax = RAxes(
            x_range=[-1, 4, 1],
            y_range=[-2, 3, 1],
        )
        x3 = ax.plot(
            lambda x: np.cos(x),
            x_range=(0, PI, 0.001)
        )

        x13 = ax.plot(
            lambda x: np.arccos(x),
            x_range=(-1, 1, 0.001)
        )

        x = ax.plot(
            lambda x: x,
            x_range=(-1, 3, 0.001),
            color=GRAY_B,
            stroke_width=1
        )

        x3_l = ax.get_graph_label(
            x3, "\\cos(x)", x_val=3, direction=UP
        )

        x13_l = ax.get_graph_label(
            x3, "\\cos^{-1}(x)", x_val=-1, direction=20*UP
        )

        self.add(ax)
        self.play(
            Succession(
                Create(x3),
                Write(x3_l)
            ),

            run_time=3
        )

        self.play(
            Create(x)
        )
        self.play(
            Succession(
                Create(x13),
                Write(x13_l)
            ),
            run_time=3
        )

        self.wait(3)


class SinInverse(Scene):
    def construct(self):
        ax = RAxes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
        )
        x3 = ax.plot(
            lambda x: np.sin(x),
            x_range=(-PI/2, PI/2, 0.001)
        )

        x13 = ax.plot(
            lambda x: np.arcsin(x),
            x_range=(-1, 1, 0.001),
            color=BLUE_B
        )

        x = ax.plot(
            lambda x: x,
            x_range=(-PI/2, PI/2, 0.001),
            color=GRAY_B,
            stroke_width=1
        )

        x3_l = ax.get_graph_label(
            x3, "\\sin(x)", x_val=PI/2, direction=UP
        )

        x13_l = ax.get_graph_label(
            x3, "\\sin^{-1}(x)", x_val=1, direction=10*UP
        )

        self.add(ax)
        self.play(
            Succession(
                Create(x3),
                Write(x3_l)
            ),

            run_time=3
        )

        self.play(
            Create(x)
        )
        self.play(
            Succession(
                Create(x13),
                Write(x13_l)
            ),
            run_time=3
        )

        self.wait(3)


class CosecInverse(Scene):
    def construct(self):
        ax = RAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
        )
        cosec_left = ax.plot(
            lambda x: 1/np.sin(x),
            x_range=(-PI/2, -0.001, 0.001)
        )

        cosec_right = ax.plot(
            lambda x: 1/np.sin(x),
            x_range=(0.001, PI/2, 0.001)
        )

        cosec_inverse_left = ax.plot(
            lambda x: np.arcsin(1/x),
            x_range=(-10, -1, 0.001),
            color=BLUE_B
        )

        cosec_inverse_right = ax.plot(
            lambda x: np.arcsin(1/x),
            x_range=(1, 10, 0.001),
            color=BLUE_B
        )

        x = ax.plot(
            lambda x: x,
            x_range=(-PI/2, PI/2, 0.001),
            color=GRAY_B,
            stroke_width=1
        )

        cosec_label = ax.get_graph_label(
            cosec_left, "\\mathrm{cosec}(x)", x_val=0.5, direction=UP
        )

        cosec_inverse_label = ax.get_graph_label(
            cosec_inverse_left, "\\mathrm{cosec}^{-1}(x)", x_val=PI, direction=UP
        )

        self.add(ax)
        self.play(
            Succession(
                Create(cosec_left),
                Create(cosec_right),
                Write(cosec_label)
            ),

            run_time=3
        )

        self.play(
            Create(x)
        )
        self.play(
            Succession(
                Create(cosec_inverse_left),
                Create(cosec_inverse_right),
                Write(cosec_inverse_label)
            ),
            run_time=3
        )

        self.wait(3)


class SecInverse(Scene):
    def construct(self):
        ax = RAxes(
            x_range=[-PI, PI, PI/2],
            y_range=[-PI, PI, PI/2],
        )
        sec_left = ax.plot(
            lambda x: 1/np.cos(x),
            x_range=(0, PI/2 - 0.001, 0.001)
        )

        sec_right = ax.plot(
            lambda x: 1/np.cos(x),
            x_range=(PI/2 + 0.001, PI, 0.001)
        )

        sec_inverse_left = ax.plot(
            lambda x: np.arccos(1/x),
            x_range=(-10, -1, 0.001),
            color=BLUE_B
        )

        sec_inverse_right = ax.plot(
            lambda x: np.arccos(1/x),
            x_range=(1, 10, 0.001),
            color=BLUE_B
        )

        x = ax.plot(
            lambda x: x,
            x_range=(-PI, PI, 0.001),
            color=GRAY_B,
            stroke_width=1
        )

        sec_label = ax.get_graph_label(
            sec_left,
            "\\mathrm{sec}(x)",
            x_val=0.25,
            direction=UP
        )

        sec_inverse_label = ax.get_graph_label(
            sec_inverse_left,
            "\\mathrm{sec}^{-1}(x)",
            x_val=PI,
            direction=UP
        )

        self.add(ax)
        self.play(
            Succession(
                Create(sec_left),
                Create(sec_right),
                Write(sec_label)
            ),

            run_time=3
        )

        self.play(
            Create(x)
        )
        self.play(
            Succession(
                Create(sec_inverse_left),
                Create(sec_inverse_right),
                Write(sec_inverse_label)
            ),
            run_time=3
        )

        self.wait(3)


s = SecInverse()
s.render()


class ThreadingAnimation(Scene):
    def construct(self):
        title = RTitle(r"$\int$")
        equation = MathTex(r"\int")

        def render_title():
            self.play(Create(title))

        def render_equation():
            self.play(Create(equation))

        thread_1 = Thread(target=render_title)
        thread_2 = Thread(target=render_equation)

        thread_1.start()
        thread_2.start()

        self.wait()
