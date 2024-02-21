from manim import *

class Limit(Scene):
    def construct(self):
        n = ValueTracker(0)
        title = Tex(
            r"\[ \lim_{x \to \infty} \left( 1 + \dfrac{1}{x} \right)^x = e \]"
        ).move_to(3*UP).scale(1.2)

        def expn(mobject):
            if int(n.get_value()) != 0:
                x = int(n.get_value())
                N = f"{x:.0e}".split('+')
                P = int(N[1])
                M = N[0].split('e')
                X = int(M[0])

                e = (1 + 1/x)**x

                if x > 1000000:
                    tex_exp = f"\\[\\left( 1 + \\dfrac{{1}}{{{X}\\times 10^{{{P}}}}} \\right)^{{{X}\\times 10^{{{P}}}}}={e:.10f}\\]"
                else:
                    tex_exp = f"\\[\\left( 1 + \\dfrac{{1}}{{{x}}} \\right)^{{{x}}}={e:.10f}\\]"
                mobject.become(
                    Tex(tex_exp).shift(2*DOWN)
                )

        E = Tex(
            r"\[ \left( 1 + \dfrac{1}{1} \right)^1 = 2 \]"
        ).shift(2*DOWN)
        E.add_updater(expn)

        self.add(n, title, E)

        self.play(
            Write(title),
            Write(E)
        )

        for i in range(2, 9):
            n.add_updater(
                lambda mobject, dt: mobject.increment_value(int(f'1e{i}')*dt)
            )
            self.wait(2)

        n.add_updater(lambda mobject, dt: mobject.increment_value(1e10*dt))
        self.wait(5)
