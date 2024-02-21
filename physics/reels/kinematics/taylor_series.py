from manim import *
from vmanim import *
from sympy import symbols, diff, pretty_print, factorial, exp, sin, cos, tan, latex, lambdify

x, y = symbols("x y")


def TS(f, a, n, l=False):

    x, y = symbols("x y")
    n = n
    x0 = a

    func = f
    result = func.subs(x, x0)

    for i in range(1, n):
        result += diff(func, x, i).subs(x, x0) * ((x - x0)**i)/(factorial(i))

    if l:
        return latex(f) + latex('=') + latex(result).replace('frac', 'dfrac')
    else:
        return lambdify(x, result)


class TaylorSeries(Scene):
    def construct(self):
        ax = RAxes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            y_length=5
        )
        self.add(ax)
        self.add(
            ax.plot(
                lambda x: sin(x),
                x_range=(-TAU, TAU, 0.01),
                color=BLUE_D
            )
        )

        def g(i):
            return ax.plot(
                TS(sin(x), 0, i),
                x_range=(-TAU, TAU, 0.01)
            )
        tg = VGroup()

        gg = VGroup()
        for i in range(1, 19):
            gg.add(g(i))
            tg.add(Title(f'${TS(sin(x), 0, i, True)}$',
                   include_underline=False).scale(0.5))
        self.play(
            Create(
                gg[0]
            ),
            Create(
                tg[0]
            )
        )
        for i in range(1, 18):
            self.play(
                Transform(gg[0], gg[i]),
                Transform(tg[0], tg[i])
            )
            self.wait()


class TaylorSeriesCos(Scene):
    def construct(self):
        ax = RAxes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            y_length=5
        )
        self.add(ax)
        self.add(
            ax.plot(
                lambda x: cos(x),
                x_range=(-TAU, TAU, 0.01),
                color=BLUE_D
            )
        )

        def g(i):
            return ax.plot(
                TS(cos(x), 0, i),
                x_range=(-TAU, TAU, 0.01)
            )
        tg = VGroup()

        gg = VGroup()
        for i in range(1, 19):
            gg.add(g(i))
            tg.add(Title(f'${TS(cos(x), 0, i, True)}$',
                   include_underline=False).scale(0.5))
        self.play(
            Create(
                gg[0]
            ),
            Create(
                tg[0]
            )
        )
        for i in range(1, 18):
            self.play(
                Transform(gg[0], gg[i]),
                Transform(tg[0], tg[i])
            )
            self.wait()


class TaylorSeriesTan(Scene):
    def construct(self):
        ax = RAxes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            y_length=5
        )
        self.add(ax)
        self.add(
            ax.plot(
                lambda x: tan(x),
                x_range=(-PI/2 + 0.1, PI/2 - 0.1, 0.001),
                color=BLUE_D
            )
        )

        def g(i):
            return ax.plot(
                TS(tan(x), 0, i),
                x_range=(-PI/2, PI/2, 0.01)
            )
        tg = VGroup()

        gg = VGroup()
        for i in range(1, 15):
            gg.add(g(i))
            tg.add(Title(f'${TS(tan(x), 0, i, True)}$',
                   include_underline=False).scale(0.5))
        self.play(
            Create(
                gg[0]
            ),
            Create(
                tg[0]
            )
        )
        for i in range(1, 14):
            self.play(
                Transform(gg[0], gg[i]),
                Transform(tg[0], tg[i])
            )
            self.wait()


class TaylorSeriesExp(Scene):
    def construct(self):
        ax = RAxes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            y_length=5
        )
        self.add(ax)
        self.add(
            ax.plot(
                lambda x: exp(x),
                x_range=(-5, 5, 0.001),
                color=BLUE_D
            )
        )

        def g(i):
            return ax.plot(
                TS(exp(x), 0, i),
                x_range=(-5, 5, 0.01)
            )
        tg = VGroup()

        gg = VGroup()
        for i in range(1, 15):
            gg.add(g(i))
            tg.add(Title(f'${TS(exp(x), 0, i, True)}$',
                   include_underline=False).scale(0.5))
        self.play(
            Create(
                gg[0]
            ),
            Create(
                tg[0]
            )
        )
        for i in range(1, 14):
            self.play(
                Transform(gg[0], gg[i]),
                Transform(tg[0], tg[i])
            )
            self.wait()
